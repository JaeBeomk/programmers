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
<!-- 상대경로 방법 -->
<!-- <link rel="stylesheet" type="text/css" href="./css/main.css" /> -->
<!-- 절대경로 방법1 : 문제점 : 프로젝트명 변경되면 망했다. 왜? 관련 1억개 파일 변경 -->
<!-- <link rel="stylesheet" type="text/css" href="/layoutMG45/css/main.css" /> -->
<!-- 절대경로 방법2 -->
<link rel="stylesheet" type="text/css" href="<%= request.getContextPath() %>/css/main.css" />
</head>
<body>
<%@ include file="/module/top.jsp" %>
<%@ include file="/module/left.jsp" %>

<%
String m_id = request.getParameter("m_id");
System.out.println(m_id + "<- m_id m_update_form.jsp");
Connection conn = null;
PreparedStatement pstmt = null;
ResultSet rs = null;
String dbid = null;
String dbpw = null;
String dblevel = null;
String dbname = null;
String dbemail = null;
//select 쿼리 실행 결과 값들을 담기 위한 변수 선언
try{
	DriverDB db = new DriverDB();
	conn = db.driverDbcon();
	pstmt = conn.prepareStatement("SELECT * FROM tb_member WHERE m_id=?");
	pstmt.setString(1, m_id);
	System.out.println(pstmt + "<-- pstmt");
	rs = pstmt.executeQuery();
	System.out.println(rs + "<-- rs m_update_form.jsp");
	//System.out.println(rs.next() + "<-- rs.next() m_update_form.jsp");
	if(rs.next()){
		System.out.println("1-1 쿼리 실행 결과 1줄 있다.");
		System.out.println(rs.getString("m_id") + "<- m_id 컬럼에 담겨있는 값");
		System.out.println(rs.getString("m_pw") + "<- m_pw 컬럼에 담겨있는 값");
		System.out.println(rs.getString("m_level") + "<- m_level 컬럼에 담겨있는 값");
		System.out.println(rs.getString("m_name") + "<- m_name 컬럼에 담겨있는 값");
		System.out.println(rs.getString("m_email") + "<- m_email 컬럼에 담겨있는 값");
//1번 방법 : 수정화면 출력 할 수 있다.		
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
	}else{
		System.out.println("1-2 쿼리 실행 결과가 없다.");
	}
} catch(SQLException ex) {
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
<!-- 2번 방법 : 처리 후 수정화면 출력 할 수 있다. -->		
<form action="<%= request.getContextPath() %>/mupdate/m_update_action.jsp" method="post">
<table border="1">
<tr>
	<td>아이디</td>
	<td><input type="text" name="m_id" size="20" value="<%= dbid %>" readonly></td>
<tr>
<tr>
	<td>암호</td>
	<td><input type="text" name="m_pw" size="20" value="<%= dbpw %>"></td>
<tr>
<tr>
	<td>권한</td>
	<td><input type="text" name="m_level" size="20" value="<%= dblevel %>"></td>
<tr>
<tr>
	<td>이름</td>
	<td><input type="text" name="m_name" size="20" value="<%= dbname %>"></td>
<tr>
<tr>
	<td>이메일</td>
	<td><input type="text" name="m_email" size="20" value="<%= dbemail %>"></td>
<tr>
<tr>
	<td colspan="4"><input type="submit" value="회원수정버튼"></td>
</tr>
</table>
</form>
<%@ include file="/module/hadan.jsp" %>
</body>
</html>

