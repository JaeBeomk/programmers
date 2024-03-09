
<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=EUC-KR">
<title>01메인화면</title>
<link rel="stylesheet" type="text/css" href="<%= request.getContextPath() %>/css/main.css" />
</head>

<body>
   
<%@ include file="/module/top.jsp" %>
<%@ include file="/module/left.jsp" %>
		       
상품등록화면 <br><br>	 
       
<form action="<%= request.getContextPath() %>/goods/goods_insert_pro.jsp" method="post">
<!-- 	<input type="hidden" name="g_code"> -->	
<table border="1">
<input type="hidden" name="m_id" value="<%= S_ID %>">
<tr>
	<td>상품명</td> 
	<td> <input type="text" name="g_name"> </td>
</tr>
<tr>
	<td>카테고리 </td> 
	<td><select name="g_cate">
		<option value="가방">가방</option>
		<option value="신발">신발</option>
	</select></td>
</tr>
<tr>
	<td>가격 </td>
	<td> <input type="text" name="g_price"> </td>
</tr>
<tr>
	<td>색상 </td>
	<td> 
	<select name="g_color">
		<option value="black">블랙</option>
		<option value="brown">브라운</option>
		<option value="red">레드</option>
		<option value="white">화이트</option>
	</select> 
	</td>
</tr>
<tr>
	<td>사이즈</td>
	<td> 
	<select name="g_size">
		<option value="S">S</option>
		<option value="M">M</option>
		<option value="L">L</option>
	</select> 
	</td>
</tr>
<tr>
	<td>상세</td>
	<td> <input type="text" name="g_desc"></td>
</tr>
<tr>
	<td>
	<input type="submit" value="상품등록버튼">
	</td>
</tr>
</table>
</form>	          		 

<%@ include file="/module/hadan.jsp" %>

   
</body>
</html>