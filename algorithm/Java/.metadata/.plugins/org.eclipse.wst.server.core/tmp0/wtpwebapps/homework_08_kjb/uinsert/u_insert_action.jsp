<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<%@ page import = "java.sql.DriverManager" %>
<%@ page import = "java.sql.Connection" %>
<%@ page import = "java.sql.PreparedStatement" %>
<%@ page import = "java.sql.SQLException" %>

<%
	request.setCharacterEncoding("euc-kr");
	Connection conn = null;
	PreparedStatement pstmt = null;
	String u_id = request.getParameter("u_id");
	String u_pw = request.getParameter("u_pw");
	String u_level = request.getParameter("u_level");
	String u_name = request.getParameter("u_name");
	String u_email = request.getParameter("u_email");
	String u_phone = request.getParameter("u_phone");
	String u_addr = request.getParameter("u_addr");
	System.out.println(u_id + "<-- u_id ");
	System.out.println(u_pw + "<-- u_pw ");
	System.out.println(u_level + "<-- u_level");
	System.out.println(u_name + "<-- u_name");
	System.out.println(u_email + "<-- u_email ");
	System.out.println(u_phone + "<-- u_phone ");
	System.out.println(u_addr + "<-- u_addr");
	
	Class.forName("com.mysql.jdbc.Driver");
	String jdbcDriver = "jdbc:mysql://localhost:3306/db08kjb?" +
			"useUnicode=true&characterEncoding=euckr";
	String dbUser = "dbid08kjb";
	String dbPass = "dbpw08kjb";
	conn = DriverManager.getConnection(jdbcDriver, dbUser, dbPass);
	System.out.println(conn + "<-- conn");
	pstmt = conn.prepareStatement(
			"INSERT INTO tb_user VALUES (?, ?, ?, ?, ?,?,?)");
	System.out.println(pstmt + "<-- pstmt 1");
	pstmt.setString(1, u_id);
	pstmt.setString(2, u_pw);
	pstmt.setString(3, u_level);
	pstmt.setString(4, u_name);
	System.out.println(pstmt + "<-- pstmt 2");
	pstmt.setString(5, u_email);
	pstmt.setString(6, u_phone);
	pstmt.setString(7, u_addr);
	System.out.println(pstmt + "<-- pstmt 3");
				
	int result = pstmt.executeUpdate();
	System.out.println(result + "<-- result");
	pstmt.close();
	conn.close();
	response.sendRedirect(request.getContextPath() + "/usearch/u_search_list.jsp");
%>