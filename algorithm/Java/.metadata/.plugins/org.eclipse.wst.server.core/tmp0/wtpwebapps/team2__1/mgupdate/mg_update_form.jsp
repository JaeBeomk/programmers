<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<%@ page import = "java.sql.DriverManager" %>
<%@ page import = "java.sql.Connection" %>
<%@ page import = "java.sql.PreparedStatement" %>
<%@ page import = "java.sql.ResultSet" %>
<%@ page import = "java.sql.SQLException" %>
<%@ page import="kr.or.ksmart.driverdb.DriverDB" %>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
<link rel="stylesheet" type="text/css" href="<%= request.getContextPath() %>/css/main.css" />
</head>
<body>
<%@ include file="/module/top.jsp" %>
<%@ include file="/module/left.jsp" %>

<%

String g_code = request.getParameter("g_code");
String m_id = request.getParameter("m_id");
String g_name = request.getParameter("g_name");
String g_cate = request.getParameter("g_cate");
String g_price = request.getParameter("g_price");
String g_color = request.getParameter("g_color");
String g_size = request.getParameter("g_size");
String g_desc = request.getParameter("g_desc");
System.out.println(g_code+ "<- g_code mg_update_form.jsp");
Connection conn = null;
PreparedStatement pstmt = null;
ResultSet rs = null;
String dbcode = null;
String dbid = null;
String dbname = null;
String dbcate = null;
String dbprice = null;
String dbcolor = null;
String dbsize = null;
String dbdate = null;
String dbdesc = null;

//select ���� ���� ��� ������ ��� ���� ���� ����
try{
	DriverDB db = new DriverDB();
	conn = db.driverDbcon();
	String select1="select1 : "+request.getParameter("select")+"��";
	pstmt = conn.prepareStatement("SELECT * FROM tb_goods WHERE g_code=?");
	pstmt.setString(1, g_code);
	System.out.println(pstmt + "<-- pstmt");
	rs = pstmt.executeQuery();
	System.out.println(rs + "<-- rs mg_update_form.jsp");
	//System.out.println(rs.next() + "<-- rs.next() m_update_form.jsp");
	if(rs.next()){
		System.out.println("1-1 ���� ���� ��� 1�� �ִ�.");

//1�� ��� : ����ȭ�� ��� �� �� �ִ�.		
		dbcode = rs.getString("g_code");
		dbid = rs.getString("m_id");
		dbname = rs.getString("g_name");
		dbcate = rs.getString("g_cate");
		dbprice = rs.getString("g_price");
		dbcolor = rs.getString("g_color");
		dbsize = rs.getString("g_size");
		dbdesc = rs.getString("g_desc");
		
	}else{
		System.out.println("1-2 ���� ���� ����� ����.");
	}
} catch(SQLException ex) {
	out.println(ex.getMessage());
	ex.printStackTrace();
} finally {
	// 6. ����� Statement ����
	if (rs != null) try { rs.close(); } catch(SQLException ex) {}
	if (pstmt != null) try { pstmt.close(); } catch(SQLException ex) {}
	
	// 7. Ŀ�ؼ� ����
	if (conn != null) try { conn.close(); } catch(SQLException ex) {}
}
%>
<!-- 2�� ��� : ó�� �� ����ȭ�� ��� �� �� �ִ�. -->		
<form action="<%= request.getContextPath() %>/mgupdate/mg_update_action.jsp" method="post">

<table border="1">
<input type="hidden" name="m_id" value="<%= S_ID %>">
<tr>
	<td>��ǰ�ڵ�</td>
	<td><input type="text" name="g_code" size="20" value="<%= dbcode %>" readonly></td>
<tr>
<tr>
	<td>�Ǹ��� ���̵�</td>
	<td><input type="text" name="m_id" size="20" value="<%= dbid %>"></td>
<tr>
<tr>
	<td>��ǰ��</td> 
	<td> <input type="text" name="g_name" value="<%= dbname %>"> </td>
</tr>
<tr>
	<td>ī�װ� </td> 
	<td><select name="g_cate" >
		<option value="����">����</option>
		<option value="�Ź�">�Ź�</option>
	</select></td>
</tr>
<tr>
	<td>���� </td>
	<td> <input type="text" name="g_price" value="<%= dbprice %>"> </td>
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
	<select name="g_size" >
		<option value="S">S</option>
		<option value="M">M</option>
		<option value="L">L</option>
	</select> 
	</td>
</tr>
<tr>
	<td>��</td>
	<td> <input type="text" name="g_desc" value="<%= dbdesc %>"></td>
</tr>
<tr>
	<td>
	<input type="submit" value="��ǰ������ư">
	</td>
</tr>
</table>
</form>
<%@ include file="/module/hadan.jsp" %>
</body>
</html>