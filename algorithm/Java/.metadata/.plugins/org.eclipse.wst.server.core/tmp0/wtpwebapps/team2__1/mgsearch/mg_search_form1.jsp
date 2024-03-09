<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">

<form action="<%=request.getContextPath()%>/mgsearch/mg_search_list1.jsp" method="post">

<select name="sk">
	<option value="g_code">상품코드</option>
	<option value="m_id">판매자아이디</option>
	<option value="g_name">상품명</option>
	<option value="g_cate">카테고리</option>
	<option value="g_color">색상</option>
	<option value="g_size">사이즈</option>
</select>
<input type="text" name="sv">
<input type="date" name="start_date">
<input type="date" name="end_date">
<input type="submit" value="검색버튼">
</form>