<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
    
<!DOCTYPE html>


<form action="<%=request.getContextPath()%>/usearch/u_search_list.jsp" method="post">
<select name="sk">
    <option value="u_id">아이디</option>
    <option value="u_level">권한</option>
    <option value="u_name">이름</option>
    <option value="u_email">이메일</option>
    <option value="u_phone">휴대폰</option>
    <option value="u_addr">주소</option>
</select>
<input type="text" name="sv">
<input type="submit" value="검색버튼">
</form>
