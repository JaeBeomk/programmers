
<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=EUC-KR">
<title>01����ȭ��</title>
<link rel="stylesheet" type="text/css" href="<%= request.getContextPath() %>/css/main.css" />
</head>

<body>
   
<%@ include file="/module/top.jsp" %>
<%@ include file="/module/left.jsp" %>
		       
��ǰ���ȭ�� <br><br>	 
       
<form action="<%= request.getContextPath() %>/goods/goods_insert_pro.jsp" method="post">
<!-- 	<input type="hidden" name="g_code"> -->	
<table border="1">
<input type="hidden" name="m_id" value="<%= S_ID %>">
<tr>
	<td>��ǰ��</td> 
	<td> <input type="text" name="g_name"> </td>
</tr>
<tr>
	<td>ī�װ� </td> 
	<td><select name="g_cate">
		<option value="����">����</option>
		<option value="�Ź�">�Ź�</option>
	</select></td>
</tr>
<tr>
	<td>���� </td>
	<td> <input type="text" name="g_price"> </td>
</tr>
<tr>
	<td>���� </td>
	<td> 
	<select name="g_color">
		<option value="black">��</option>
		<option value="brown">����</option>
		<option value="red">����</option>
		<option value="white">ȭ��Ʈ</option>
	</select> 
	</td>
</tr>
<tr>
	<td>������</td>
	<td> 
	<select name="g_size">
		<option value="S">S</option>
		<option value="M">M</option>
		<option value="L">L</option>
	</select> 
	</td>
</tr>
<tr>
	<td>��</td>
	<td> <input type="text" name="g_desc"></td>
</tr>
<tr>
	<td>
	<input type="submit" value="��ǰ��Ϲ�ư">
	</td>
</tr>
</table>
</form>	          		 

<%@ include file="/module/hadan.jsp" %>

   
</body>
</html>