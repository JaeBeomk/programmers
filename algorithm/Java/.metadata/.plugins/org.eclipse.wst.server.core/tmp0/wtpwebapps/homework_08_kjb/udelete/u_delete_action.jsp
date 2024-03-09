<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<%@ page import = "java.sql.DriverManager" %>
<%@ page import = "java.sql.Connection" %>
<%@ page import = "java.sql.PreparedStatement" %>
<%@ page import = "java.sql.SQLException" %>
<%
	String send_id = request.getParameter("send_id");
	System.out.println(send_id + "<- send_id");
	Connection conn = null;
	PreparedStatement pstmt = null;
	Class.forName("com.mysql.jdbc.Driver");
	String jdbcDriver = "jdbc:mysql://localhost:3306/db08kjb?" +
			"useUnicode=true&characterEncoding=euckr";
	String dbUser = "dbid08kjb";
	String dbPass = "dbpw08kjb";
	conn = DriverManager.getConnection(jdbcDriver, dbUser, dbPass);
	System.out.println(conn + "<-- conn");
	
	pstmt = conn.prepareStatement(
			"DELETE FROM tb_user WHERE u_id=?");
	pstmt.setString(1, send_id);
	System.out.println(pstmt + "<-- pstmt 1");
	int result = pstmt.executeUpdate();
	System.out.println(result + "<-- result");
	
	
	response.sendRedirect(request.getContextPath() + "/usearch/u_search_list.jsp");

%>
