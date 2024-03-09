<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<%@ page import = "java.sql.DriverManager" %>
<%@ page import = "java.sql.Connection" %>
<%@ page import = "java.sql.PreparedStatement" %>
<%@ page import = "java.sql.ResultSet" %>
<%@ page import = "java.sql.SQLException" %>
<%
String m_id = request.getParameter("m_id");
System.out.println(m_id + "<- m_id m_update_form.jsp");
Connection conn = null;
PreparedStatement pstmt = null;
ResultSet rs = null;
Class.forName("com.mysql.jdbc.Driver");
String dbid = null;
String dbpw = null;
String dblevel = null;
String dbname = null;
String dbemail = null;
//select ���� ���� ��� ������ ��� ���� ���� ����
try{
	String jdbcDriver = "jdbc:mysql://localhost:3306/dev45db?" +
			"useUnicode=true&characterEncoding=euckr";
	String dbUser = "dev45id";
	String dbPass = "dev45pw";
	conn = DriverManager.getConnection(jdbcDriver, dbUser, dbPass);
	System.out.println(conn + "<-- conn m_update_form.jsp");
	pstmt = conn.prepareStatement("SELECT * FROM tb_member WHERE m_id=?");
	pstmt.setString(1, m_id);
	System.out.println(pstmt + "<-- pstmt");
	rs = pstmt.executeQuery();
	System.out.println(rs + "<-- rs m_update_form.jsp");
	//System.out.println(rs.next() + "<-- rs.next() m_update_form.jsp");
	if(rs.next()){
		System.out.println("1-1 ���� ���� ��� 1�� �ִ�.");
		System.out.println(rs.getString("m_id") + "<- m_id �÷��� ����ִ� ��");
		System.out.println(rs.getString("m_pw") + "<- m_pw �÷��� ����ִ� ��");
		System.out.println(rs.getString("m_level") + "<- m_level �÷��� ����ִ� ��");
		System.out.println(rs.getString("m_name") + "<- m_name �÷��� ����ִ� ��");
		System.out.println(rs.getString("m_email") + "<- m_email �÷��� ����ִ� ��");
//1�� ��� : ����ȭ�� ��� �� �� �ִ�.		
		dbid = rs.getString("m_id");
		dbpw = rs.getString("m_pw");
		dblevel = rs.getString("m_level");
		dbname = rs.getString("m_name");
		dbemail = rs.getString("m_email");
		System.out.println(dbid + "<- dbid ������ ����ִ� ��");
		System.out.println(dbpw + "<- dbpw ������ ����ִ� ��");
		System.out.println(dblevel + "<- dblevel ������ ����ִ� ��");
		System.out.println(dbname + "<- dbname ������ ����ִ� ��");
		System.out.println(dbemail + "<- dbemail ������ ����ִ� ��");
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
<form action="<%= request.getContextPath() %>/mupdate/m_update_action.jsp" method="post">
<table border="1">
<tr>
	<td>���̵�</td>
	<td><input type="text" name="m_id" size="20" value="<%= dbid %>" readonly></td>
<tr>
<tr>
	<td>��ȣ</td>
	<td><input type="text" name="m_pw" size="20" value="<%= dbpw %>"></td>
<tr>
<tr>
	<td>����</td>
	<td><input type="text" name="m_level" size="20" value="<%= dblevel %>"></td>
<tr>
<tr>
	<td>�̸�</td>
	<td><input type="text" name="m_name" size="20" value="<%= dbname %>"></td>
<tr>
<tr>
	<td>�̸���</td>
	<td><input type="text" name="m_email" size="20" value="<%= dbemail %>"></td>
<tr>
<tr>
	<td colspan="4"><input type="submit" value="ȸ��������ư"></td>
</tr>
</table>
</form>











<!-- 
m_list.jsp
1) ������ư Ŭ���ÿ� get������� ���̵� ���� �ѱ��
m_update_form.jsp
2) ���̵� ���� �޾Ƽ� �ܼ�â�� Ȯ���Ѵ�
3) ����̹��ε� 4) DB����
5) �������� �غ� SELECT * FROM tb_member WHERE m_id=?
SELECT * FROM tb_member WHERE m_id='id002' <-- �������� �ϼ�
6) ���� ���� 
7) ���������� ( ���� ȭ�鿡 �ѷ��ش� ) : 
 ù��° ó�������� ����ȭ���� �Ѹ��� ��� / �ι�° ���� ȭ�� ������ �����ϰ� ���� �Ѹ����� �غ���!
8)9)10) ��ü����
-->