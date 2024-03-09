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
		System.out.println("1-1 아이디 일치");
		dbid = rs.getString("m_id");
		dbpw = rs.getString("m_pw");
		dblevel = rs.getString("m_level");
		dbname = rs.getString("m_name");
		dbemail = rs.getString("m_email");
		System.out.println(dbid + "<- dbid 변수에 담겨있는 값");
		System.out.println(dbpw + "<- dbpw 변수에 담겨있는 값");
		System.out.println(dblevel + "<- dblevel 변수에 담겨있는 값");
		System.out.println(dbname + "<- dbname 변수에 담겨있는 값");
		System.out.println(dbemail + "<- dbemail 변수에 담겨있는 값");
		if(pw.equals(dbpw)){
			System.out.println("2-1 로그인성공");	
			session.setAttribute("S_ID", dbid);
			session.setAttribute("S_NAME", dbname);
			session.setAttribute("S_LEVEL", dblevel);
			msg = "로그인성공";
		}else{
			System.out.println("2-2 비번 불일치");
			msg = "비번 불일치";
		}
	}else{
		System.out.println("1-2 아이디 불일치");
		msg = "아이디불일치";
	}
}catch(SQLException ex) {
	out.println(ex.getMessage());
	ex.printStackTrace();
} finally {
	// 6. 사용한 Statement 종료
	if (rs != null) try { rs.close(); } catch(SQLException ex) {}
	if (pstmt != null) try { pstmt.close(); } catch(SQLException ex) {}
	
	// 7. 커넥션 종료
	if (conn != null) try { conn.close(); } catch(SQLException ex) {}
}

%>
<script type="text/javascript">
	alert('<%= msg %>');
	location.href='<%= request.getContextPath()%>/index.jsp';
</script>