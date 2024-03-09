<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<%@ page import="java.sql.DriverManager"%>
<%@ page import="java.sql.Connection"%>
<%@ page import="java.sql.PreparedStatement"%>
<%@ page import="java.sql.ResultSet"%>
<%@ page import="java.sql.SQLException"%>
<%@ page import="kr.or.ksmart.driverdb.DriverDB" %>
<%

String id = request.getParameter("id");
String pw = request.getParameter("pw");
%>

<%
	request.setCharacterEncoding("euc-kr");
	Connection conn = null;
	PreparedStatement pstmt = null;
	ResultSet rs = null;
	String msg = null;
	String dbid = null;
	String dbpw = null;
	String dblevel = null;
	String dbname = null;
	String dbemail = null;

	try {
		DriverDB db = new DriverDB();
		conn = db.driverDbcon();
		
		pstmt = conn.prepareStatement("SELECT * FROM tb_member WHERE m_id=?");
		
		pstmt.setString(1, id);
		System.out.println(pstmt + "<-- pstmt 1");
		
		rs = pstmt.executeQuery();
		
		if(rs.next()){
			System.out.println("1-1 ���̵� ��ġ");
			dbid = rs.getString("m_id");
			dbpw = rs.getString("m_pw");
			dblevel = rs.getString("m_level");
			dbname = rs.getString("m_name");
			System.out.println(dbid + "<- dbid ������ ����ִ� ��");
			System.out.println(dbpw + "<- dbpw ������ ����ִ� ��");
			System.out.println(dblevel + "<- dblevel ������ ����ִ� ��");
			System.out.println(dbname + "<- dbname ������ ����ִ� ��");
			System.out.println(dbemail + "<- dbemail ������ ����ִ� ��");
			if(pw.equals(dbpw)){
				System.out.println("2-1 �α��� ����");
				session.setAttribute("S_ID", dbid);
				session.setAttribute("S_NAME", dbname);
				session.setAttribute("S_LEVEL", dblevel);
				msg = "�α��� ����";
			}else{
				System.out.println("2-2 ��й�ȣ ����ġ");
				msg = "��й�ȣ ����ġ";
			}
		}else{
			System.out.println("1-2 ���̵� ����ġ");
			msg = "���̵� ����ġ";
		}
	
}catch(SQLException ex) {
	out.println(ex.getMessage());
	ex.printStackTrace();	
}finally{

	if (pstmt != null) try { pstmt.close(); } catch(SQLException ex) {}
	if (conn != null) try { conn.close(); } catch(SQLException ex) {}
}	
%>

<script type="text/javascript">
	alert('<%= msg %>');
	location.href='<%= request.getContextPath()%>/index.jsp';
</script>