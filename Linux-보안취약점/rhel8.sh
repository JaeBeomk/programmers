#! /bin/bash


# rhel8 버전 보안취약점
# sudo -i # root user로 진행
# 전체 보안취약점 중 몇가지만 사용 예정

host=`hostname`
date=`date +%y%0m%d`

##### setting ####
# middle ware home dir

##### su user ####
su_user='실제 관리자 계정 - no root'

echo "rhel 8 security" > "$host"_"$date".txt
echo "========================================================================================" >> "$host"_"$date".txt
echo "" >> "$host"_"$date".txt
##### U-01 #######
# ssh root login deny
ssh_c=`cat /etc/ssh/sshd_config | grep 'PermitRootLogin no' | grep -v "^#" | wc -l`
if [ "$ssh_c" -lt 1 ]
then
/usr/bin/cp /etc/ssh/sshd_config /etc/ssh/sshd_config_bak
sed -i "s/PermitRootLogin yes/#PermitRootLogin yes\nPermitRootLogin no/g" /etc/ssh/sshd_config
else
 echo "/etc/ssh/sshd_config 확인 필요"
fi

echo "ssh root login deny " >> "$host"_"$date".txt
cat /etc/ssh/sshd_config | grep 'PermitRootLogin' | grep -v "^#" >> "$host"_"$date".txt

echo "" >> "$host"_"$date".txt
echo "========================================================================================" >> "$host"_"$date".txt
echo "" >> "$host"_"$date".txt



## /etc/security/pwquality.conf
pwq_c=`cat /etc/security/pwquality.conf | grep 'minlen = 8' | grep -v "^#" | wc -l`
if [ "$pwq_c" -lt 1 ]
then
/usr/bin/cp /etc/security/pwquality.conf /etc/security/pwquality.conf_bak
sed -i "s/# minlen = 8/# minlen = 8\n minlen = 9/g" /etc/security/pwquality.conf
sed -i "s/# dcredit = 0/# dcredit = 0\n dcredit = 1/g" /etc/security/pwquality.conf
sed -i "s/# ucredit = 0/# ucredit = 0\n ucredit = 1/g" /etc/security/pwquality.conf
sed -i "s/# lcredit = 0/# lcredit = 0\n lcredit = 1/g" /etc/security/pwquality.conf
sed -i "s/# ocredit = 0/# ocredit = 0\n ocredit = 1/g" /etc/security/pwquality.conf
sed -i 's/# maxrepeat = 0/# maxrepeat = 0\n maxrepeat = 3/g' /etc/security/pwquality.conf
sed -i 's/# maxclassrepeat = 0/# maxclassrepeat = 0 \n maxclassrepeat = 3/g' /etc/security/pwquality.conf
sed -i 's/# retry = 3/# retry = 3\n retry = 3/g' /etc/security/pwquality.conf
else
 echo "/etc/security/pwquality.conf 확인 필요" >> "$host"_"$date".txt
fi

echo "" >> "$host"_"$date".txt
echo "========================================================================================" >> "$host"_"$date".txt
echo "" >> "$host"_"$date".txt

## /etc/pam.d/system-auth
## root 적용시
sys_auth=`cat /etc/pam.d/system-auth | grep local_users_only |grep -v "^#"| wc -l`
if [ "$sys_auth" -ge 1];then
sed -i 's/pam_pwquality.so try_first_pass local_users_only/pam_pwquality.so try_first_pass enforce_for_root/g' system-auth
sed -i 's/pam_pwquality.so try_first_pass local_users_only/pam_pwquality.so try_first_pass enforce_for_root/g' password-auth

sed -i '/pam_env.so/a\auth        required        pam_faillock.so preauth silent audit deny=5 unlock_time=600' system-auth.bak
sed -i '/pam_unix.so nullok try_first_pass/a\auth        [default=die]   pam_faillock.so authfail audit deny=5 unlock_time=600' system-auth.bak
sed -i '/pam_permit.so/a\account     required        pam_faillock.so' system-auth.bak

## root 적용시
sed -i 's/pam_faillock.so preauth silent audit deny=5/pam_faillock.so preauth silent audit deny=5 even_deny_root unlock_time=600/g' system-auth.bak
sed -i 's/authfail audit deny=5 unlock_time=600/authfail audit deny=5 even_deny_root unlock_time=600/g' system-auth.bak
else
    echo "/etc/pam.d/system-auth or /etc/pam.d/password-auth 확인 필요" >> "$host"_"$date".txt

fi
echo "" >> "$host"_"$date".txt
echo "========================================================================================" >> "$host"_"$date".txt
echo "" >> "$host"_"$date".txt

xinet=`ls -al /etc/xinetd.d/ | wc -l`
if [ "$xinet" -eq 3];then
echo "xinetd 무시"  >> "$host"_"$date".txt
else
ls -la /etc/xinetd.conf >> "$host"_"$date".txt
ls -la /etc/xinetd.conf 2>> "$host"_"$date".txt
ls -la /etc/xinetd.d/ >> "$host"_"$date".txt
fi

echo "" >> "$host"_"$date".txt
echo "========================================================================================" >> "$host"_"$date".txt
echo "" >> "$host"_"$date".txt
echo "crond file owner & permit check " >> "$host"_"$date".txt

cron_c=`ls -alrt /etc/cron.* | grep rwx | grep -v drwx`
if [ "$cron_c"  -ge 1 ];then
    chmod 640 /etc/cron*/*
else
    "/etc/cron* 확인 필요" >> "$host"_"$date".txt
fi


echo "" >> "$host"_"$date".txt
echo "========================================================================================" >> "$host"_"$date".txt
echo "" >> "$host"_"$date".txt

tm_c=`cat /etc/profile | grep TMOUT | wc -l`
if [ "$tm_c" -eq 0 ]; then
echo 'export TMOUT = 300' >> /etc/profile

else
echo "/etc/profile 확인 필요"
fi

echo "" >> "$host"_"$date".txt
echo "========================================================================================" >> "$host"_"$date".txt
echo "유저없는 파일 삭제" >> "$host"_"$date".txt

no_ug=`find / -nouser 2>/dev/null | wc -l`
if [ "$no_ug" -ne 0 ]; then
rm  -rf `find / -nouser 2>/dev/null`
else
echo "find / -nouser 2>/dev/null 확인 필요" >>"$host"_"$date".txt

fi


echo "" >> "$host"_"$date".txt
echo "========================================================================================" >> "$host"_"$date".txt

echo "root su limit " >> "$host"_"$date".txt

if [ -f "/etc/pam.d/su_bak" ] ;
then
echo "수행 없었음 " >> "$host"_"$date".txt
else
/usr/bin/cp /etc/pam.d/su /etc/pam.d/su_bak
sed 's/#auth           required        pam_wheel.so use_uid/auth           required        pam_wheel.so use_uid # 주석제거/g ' /etc/pam.d/su
sed -i "s/wheel:x:10:/wheel:x:10:root,$su_user/g" /etc/group
chown root:wheel /usr/bin/su
chmod 4750 /usr/bin/su
fi

echo "" >> "$host"_"$date".txt
echo "========================================================================================" >> "$host"_"$date".txt
echo "" >> "$host"_"$date".txt


if [ -f "/etc/login.defs_bak" ] ;
then
echo "수행 없었음 " >> "$host"_"$date".txt
else
/usr/bin/cp /etc/login.defs /etc/login.defs_bak

sed -i 's/^PASS_MAX_DAYS\s\+99999/PASS_MAX_DAYS   90/' /etc/login.defs
sed -i 's/^PASS_MIN_DAYS\s\+0/PASS_MIN_DAYS   1/' /etc/login.defs
sed -i 's/^PASS_MIN_LEN\s\+5/PASS_MIN_LEN    8/' /etc/login.defs
sed -i 's/^PASS_WARN_AGE\s\+7/PASS_WARN_AGE   7/' /etc/login.defs
fi

echo "" >> "$host"_"$date".txt
echo "========================================================================================" >> "$host"_"$date".txt
echo "" >> "$host"_"$date".txt

echo "rsyslog config" >> "$host"_"$date".txt
alert_c=`cat /etc/rsyslog.conf | grep alert`
if [ "$alert_c" -eq 0 ]; then
echo '*.alert                                                 /dev/console' >> /etc/rsyslog.conf
fi


echo "" >> "$host"_"$date".txt
echo "========================================================================================" >> "$host"_"$date".txt
echo "계정 비밀 번호 기간 설정" >> "$host"_"$date".txt

# ex) chage -I 7 -m 0 -M 30 test1
if [ "$(ls /home/|wc -l)" -ne 0 ];then
    for i in $(ls /home/|awk '{print $0}');do
        chage -I 7 -m 0 -M 30 $i
    done
fi
