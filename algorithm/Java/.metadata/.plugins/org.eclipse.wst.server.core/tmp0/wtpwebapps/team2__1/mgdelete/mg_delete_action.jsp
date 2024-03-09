<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<%@ page import = "java.sql.DriverManager" %>
<%@ page import = "java.sql.Connection" %>
<%@ page import = "java.sql.PreparedStatement" %>
<%@ page import = "java.sql.SQLException" %>
<%@ page import="kr.or.ksmart.driverdb.DriverDB" %>
<%@ page import="kr.or.ksmart.dto.Goods" %>
<%@ page import="kr.or.ksmart.dao.Gdao"%>
<% request.setCharacterEncoding("euc-kr");	//post방식 한글처리 %>
<jsp:useBean id="g" class="kr.or.ksmart.dto.Goods"/>
<jsp:setProperty name="g" property="*"/>
<%

String g_code = request.getParameter("g_code");
Gdao gdao=new Gdao();
gdao.mgDelete(g);
response.sendRedirect(request.getContextPath()+"/mgsearch/mg_search_list1.jsp");
%>