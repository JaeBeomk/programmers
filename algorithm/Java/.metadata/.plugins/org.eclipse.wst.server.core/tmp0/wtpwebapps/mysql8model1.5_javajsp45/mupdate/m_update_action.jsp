<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<%@ page import = "java.sql.DriverManager" %>
<%@ page import = "java.sql.Connection" %>
<%@ page import = "java.sql.PreparedStatement" %>
<%@ page import = "java.sql.SQLException" %>
<%@ page import="kr.or.ksmart.driverdb.DriverDB" %>
<%@ page import="kr.or.ksmart.dto.Member" %>
<%@ page import="kr.or.ksmart.dao.Mdao" %>

<% request.setCharacterEncoding("euc-kr");	//post방식 한글처리 %>
<jsp:useBean id="m" class="kr.or.ksmart.dto.Member"/>
<jsp:setProperty name="m" property="*"/>

<%
Mdao mdao=new Mdao();
mdao.mUpdate(m);
response.sendRedirect(request.getContextPath()+"/msearch/m_search_list.jsp");
%>