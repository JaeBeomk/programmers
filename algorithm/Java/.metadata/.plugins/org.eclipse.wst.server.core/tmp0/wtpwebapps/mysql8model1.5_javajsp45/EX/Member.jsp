<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<%@ page import="kr.or.ksmart.dto.Member" %>

<%
Member m = new Member();
m.setM_id("id001");
m.setM_pw("pw001");
m.setM_level("구매자");
m.setM_name("일길동");
m.setM_email("email01");

System.out.println(m + "<- m");
%>