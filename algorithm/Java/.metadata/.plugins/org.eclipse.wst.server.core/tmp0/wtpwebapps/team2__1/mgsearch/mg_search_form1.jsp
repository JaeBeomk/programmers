<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">

<form action="<%=request.getContextPath()%>/mgsearch/mg_search_list1.jsp" method="post">

<select name="sk">
	<option value="g_code">��ǰ�ڵ�</option>
	<option value="m_id">�Ǹ��ھ��̵�</option>
	<option value="g_name">��ǰ��</option>
	<option value="g_cate">ī�װ�</option>
	<option value="g_color">����</option>
	<option value="g_size">������</option>
</select>
<input type="text" name="sv">
<input type="date" name="start_date">
<input type="date" name="end_date">
<input type="submit" value="�˻���ư">
</form>