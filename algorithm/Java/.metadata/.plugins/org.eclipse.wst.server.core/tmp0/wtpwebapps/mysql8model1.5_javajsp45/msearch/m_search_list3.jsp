<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<%@ page import = "java.sql.DriverManager" %>
<%@ page import = "java.sql.Connection" %>
<%@ page import = "java.sql.PreparedStatement" %>
<%@ page import = "java.sql.ResultSet" %>
<%@ page import = "java.sql.SQLException" %>

<%@ include file="/msearch/m_search_form.jsp" %>

<%
request.setCharacterEncoding("euc-kr");
String sk = request.getParameter("sk");
String sv = request.getParameter("sv");
//3�ܰ� : ���� ���� �غ� �ܰ� : m_list.jsp�� �����ϴ�

Connection conn = null;
PreparedStatement pstmt = null;
ResultSet rs = null;
Class.forName("com.mysql.jdbc.Driver");
try{
	String jdbcDriver = "jdbc:mysql://localhost:3306/dev45db?" +
			"useUnicode=true&characterEncoding=euckr";
	String dbUser = "dev45id";
	String dbPass = "dev45pw";
	conn = DriverManager.getConnection(jdbcDriver, dbUser, dbPass);
	System.out.println(conn + "<-- conn m_search_list.jsp");
	if(sk == null && sv == null){
		System.out.println("1-1 sk,sv �Ѵ� null ����");
		pstmt = conn.prepareStatement("select * from tb_member");
		System.out.println(pstmt + "<-- pstmt");
	}else if(sk != null && sv.equals("")){
		System.out.println("1-2 sk�� null�ƴϰ� sv�� ���� ����");
		pstmt = conn.prepareStatement("select * from tb_member");
		System.out.println(pstmt + "<-- pstmt");
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




