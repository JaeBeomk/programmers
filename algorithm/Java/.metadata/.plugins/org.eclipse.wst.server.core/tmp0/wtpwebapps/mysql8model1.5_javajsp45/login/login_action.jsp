<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<%@ page import = "java.sql.DriverManager" %>
<%@ page import = "java.sql.Connection" %>
<%@ page import = "java.sql.PreparedStatement" %>
<%@ page import = "java.sql.ResultSet" %>
<%@ page import = "java.sql.SQLException" %>
<%@ page import="kr.or.ksmart.driverdb.DriverDB" %>

<%
String id = request.getParameter("id");
String pw = request.getParameter("pw");
System.out.println(id + "<- id login_action.jsp");
System.out.println(pw + "<- pw login_action.jsp");
Connection conn = null;
PreparedStatement pstmt = null;
ResultSet rs = null;
String dbid = null;
String dbpw = null;
String dblevel = null;
String dbname = null;
String dbemail = null;
String msg = null;

try{
	DriverDB db = new DriverDB();
	conn = db.driverDbcon();
	System.out.println(conn + "<-- conn login_action.jsp");
	pstmt = conn.prepareStatement("SELECT * FROM tb_member WHERE m_id=?");
	pstmt.setString(1, id);
	System.out.println(pstmt + "<-- pstmt");
	rs = pstmt.executeQuery();
	if(rs.next()){
		System.out.println("1-1 ���̵� ��ġ");
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
		if(pw.equals(dbpw)){
			System.out.println("2-1 �α��μ���");	
			session.setAttribute("S_ID", dbid);
			session.setAttribute("S_NAME", dbname);
			session.setAttribute("S_LEVEL", dblevel);
			msg = "�α��μ���";
		}else{
			System.out.println("2-2 ��� ����ġ");
			msg = "��� ����ġ";
		}
	}else{
		System.out.println("1-2 ���̵� ����ġ");
		msg = "���̵����ġ";
	}
}catch(SQLException ex) {
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
<script type="text/javascript">
	alert('<%= msg %>');
	location.href='<%= request.getContextPath()%>/index.jsp';
</script>