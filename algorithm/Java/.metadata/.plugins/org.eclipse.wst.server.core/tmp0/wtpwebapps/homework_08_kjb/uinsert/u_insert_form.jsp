<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=EUC-KR">
<title>Insert title here</title>
<!-- <link rel="stylesheet" type="text/css" href="/layoutMG/css/main.css" /> -->
<link rel="stylesheet" type="text/css" href="<%= request.getContextPath() %>/css/main2.css" />
</head>

<body>
<%@ include file="/module/top.jsp" %>
<%@ include file="/module/left.jsp" %>


<form action="<%= request.getContextPath() %>/uinsert/u_insert_action.jsp" method="post">
<table border="1">
<tr>
	<td>���̵�</td>
	<td><input type="text" name="u_id" size="20"></td>
<tr>
<tr>
	<td>��ȣ</td>
	<td><input type="text" name="u_pw" size="20"></td>
<tr>
<tr>
	<td>����</td>
	<td><input type="text" name="u_level" size="20"></td>
<tr>
<tr>
	<td>�̸�</td>
	<td><input type="text" name="u_name" size="20"></td>
<tr>
<tr>
	<td>�̸���</td>
	<td><input type="text" name="u_email" size="20"></td>
<tr>
<tr>
	<td>�޴���</td>
	<td><input type="text" name="u_phone" size="20"></td>
<tr>
<tr>
	<td>�ּ�</td>
	<td><input type="text" name="u_addr" size="20"></td>
<tr>
<tr>
	<td colspan="4"><input type="submit" value="ȸ�����Թ�ư"></td>
</tr>
</table>
</form>

<%@ include file="/module/hadan.jsp" %>

</body>
</html>