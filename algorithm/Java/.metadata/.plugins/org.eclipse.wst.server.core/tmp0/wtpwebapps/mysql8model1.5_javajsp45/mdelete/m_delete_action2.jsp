<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<%@ page import = "java.sql.DriverManager" %>
<%@ page import = "java.sql.Connection" %>
<%@ page import = "java.sql.PreparedStatement" %>
<%@ page import = "java.sql.SQLException" %>
<%@ page import="kr.or.ksmart.driverdb.DriverDB" %>

<%
String m_id = request.getParameter("m_id");
System.out.println(m_id + "<- m_id m_delete_action.jsp");
Connection conn = null;
PreparedStatement pstmt = null;
DriverDB db = new DriverDB();
conn = db.driverDbcon();
System.out.println(conn + "<-- conn");
pstmt = conn.prepareStatement("DELETE FROM tb_member WHERE m_id=?");
pstmt.setString(1, m_id);
System.out.println(pstmt + "<-- pstmt 1");
int result = pstmt.executeUpdate();
System.out.println(result + "<-- result");
pstmt.close();
conn.close();
//response.sendRedirect(request.getContextPath()+"/mlist/m_list.jsp");
response.sendRedirect(request.getContextPath()+"/msearch/m_search_list.jsp");
%>