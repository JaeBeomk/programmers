<%@ page language="java" contentType="text/html; charset=EUC-KR"
	pageEncoding="EUC-KR"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<%@ page import="java.sql.DriverManager"%>
<%@ page import="java.sql.Connection"%>
<%@ page import="java.sql.PreparedStatement"%>
<%@ page import="java.sql.SQLException"%>
<%@ page import="kr.or.ksmart.driverdb.DriverDB" %>

<% request.setCharacterEncoding("euc-kr");	//post规侥 茄臂贸府 %>
<jsp:useBean id="m" class="kr.or.ksmart.dto.Member"/>
<jsp:setProperty name="m" property="*"/>
<%
Connection conn = null;
PreparedStatement pstmt = null;

DriverDB db = new DriverDB();
conn = db.driverDbcon();		
pstmt = conn.prepareStatement(
		"INSERT INTO tb_member VALUES (?, ?, ?, ?, ?)");
System.out.println(pstmt + "<-- pstmt 1");
System.out.println(m + "<-- m");

//Member按眉俊辑 百泼 饶 insert孽府 肯己
pstmt.setString(1, m.getM_id());
pstmt.setString(2, m.getM_pw());
pstmt.setString(3, m.getM_level());
pstmt.setString(4, m.getM_name());
pstmt.setString(5, m.getM_email());

System.out.println(pstmt + "<-- pstmt 2");
int result = pstmt.executeUpdate();
System.out.println(result + "<-- result");

pstmt.close();
pstmt.close();
response.sendRedirect(request.getContextPath()+"/msearch/m_search_list.jsp");	

%>