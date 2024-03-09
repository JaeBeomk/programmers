<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<%
String id = request.getParameter("id");
String pw = request.getParameter("pw");
System.out.println(id + "<- id login_action.jsp");
System.out.println(pw + "<- pw login_action.jsp");
// 가입된 회원정보
String dbid = "id001";
String dbpw = "pw001";
String dbname = "홍길동";
String dblevel = "관리자";	
//최고관리자 또는 관리자 또는 판매자 또는 구매자 권한 변경 후 테스트
String msg = null;
if(id.equals(dbid)){
	System.out.println("1-1 아이디 일치");
	if(pw.equals(dbpw)){
		System.out.println("2-1 로그인성공");	
		//세션 객체(영역)에 셋팅
		session.setAttribute("S_ID", dbid);
		session.setAttribute("S_NAME", dbname);
		session.setAttribute("S_LEVEL", dblevel);
		//response.sendRedirect(request.getContextPath()+"/index.jsp");
		msg = "로그인성공";
	}else{
		System.out.println("2-2 비번 불일치");
		msg = "비번 불일치";
	}
}else{
	System.out.println("1-2 아이디 불일치");
	msg = "아이디불일치";
}
%>
<script type="text/javascript">
	alert('<%= msg %>');
	location.href='<%= request.getContextPath()%>/index.jsp';
</script>