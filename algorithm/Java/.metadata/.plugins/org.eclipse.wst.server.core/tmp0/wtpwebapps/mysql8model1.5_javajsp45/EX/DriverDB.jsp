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
driverDbcon �޼��� ȣ�� �� ���ϰ��� �޾�
���ο� ���� conn�� �Ҵ�(����,�Է�) ��
�ܼ�â�� ����ϼ���!
 -->