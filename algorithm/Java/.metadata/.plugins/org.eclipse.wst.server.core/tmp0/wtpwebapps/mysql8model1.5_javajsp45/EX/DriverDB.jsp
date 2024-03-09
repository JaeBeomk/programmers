<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<%@ page import="kr.or.ksmart.driverdb.DriverDB" %>
<%@ page import="java.sql.Connection" %>
<%
Connection conn = null;
DriverDB db = new DriverDB();
conn = db.driverDbcon();
System.out.println(conn + "<- conn");
%>

<!-- 
driverDbcon 메서드 호출 후 리턴값을 받아
새로운 변수 conn에 할당(대입,입력) 후
콘솔창에 출력하세요!
 -->