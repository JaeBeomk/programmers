<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
    
<!DOCTYPE html>


<form action="<%=request.getContextPath()%>/usearch/u_search_list.jsp" method="post">
<select name="sk">
    <option value="u_id">���̵�</option>
    <option value="u_level">����</option>
    <option value="u_name">�̸�</option>
    <option value="u_email">�̸���</option>
    <option value="u_phone">�޴���</option>
    <option value="u_addr">�ּ�</option>
</select>
<input type="text" name="sv">
<input type="submit" value="�˻���ư">
</form>
