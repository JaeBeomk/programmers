<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<%@ page import = "java.sql.DriverManager" %>
<%@ page import = "java.sql.Connection" %>
<%@ page import = "java.sql.PreparedStatement" %>
<%@ page import = "java.sql.ResultSet" %>
<%@ page import = "java.sql.SQLException" %>
<%@ include file="/uinsert/u_insert_form.jsp" %>


ȸ�� ����Ʈ <br>
<table width="100%" border="1">
<tr>
	<td>���̵�</td><td>���</td><td>����</td><td>�̸�</td><td>�̸���</td><td>�޴���</td><td>�ּ�</td><td>����</td><td>����</td>
</tr>

<%
Connection conn = null;
PreparedStatement pstmt = null;
ResultSet rs = null;
Class.forName("com.mysql.jdbc.Driver");

try{
	String jdbcDriver = "jdbc:mysql://localhost:3306/db08kjb?" +
			"useUnicode=true&characterEncoding=euckr";
	String dbUser = "dbid08kjb";
	String dbPass = "dbpw08kjb";
	conn = DriverManager.getConnection(jdbcDriver, dbUser, dbPass);
	System.out.println(conn + "<-- conn");
	if(conn != null){
		out.println("01 DB���� ����");
	}else{
		out.println("02 DB���� ����");
	}
	pstmt = conn.prepareStatement("SELECT * FROM tb_user");
	rs = pstmt.executeQuery();
	System.out.println(rs + "<-- rs");
	while(rs.next()){
		System.out.println("while����");
%>
		<tr>
			<td><%= rs.getString("u_id")%></td>
			<td><%= rs.getString("u_pw")%></td>
			<td><%= rs.getString("u_level")%></td>
			<td><%= rs.getString("u_name")%></td>
			<td><%= rs.getString("u_email")%></td>
			<td><%= rs.getString("u_phone")%></td>
			<td><%= rs.getString("u_addr")%></td>
			<td>
			<a href="<%= request.getContextPath() %>/uupdate/u_update_form.jsp?send_id=<%= rs.getString("u_id")%>">������ư</a>			
			</td>
			<td>
			<a href="<%= request.getContextPath() %>/udelete/u_delete_action.jsp?send_id=<%= rs.getString("u_id")%>">������ư</a>			
			</td>
		</tr>
<%		
	}
}catch(SQLException ex) {
	out.println(ex.getMessage());
	ex.printStackTrace();
} finally {
	if (rs != null) try { rs.close(); } catch(SQLException ex) {}
	if (pstmt != null) try { pstmt.close(); } catch(SQLException ex) {}
	if (conn != null) try { conn.close(); } catch(SQLException ex) {}
}
%>
</table>