<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<%@ page import = "java.sql.DriverManager" %>
<%@ page import = "java.sql.Connection" %>
<%@ page import = "java.sql.PreparedStatement" %>
<%@ page import = "java.sql.ResultSet" %>
<%@ page import = "java.sql.SQLException" %>

<%
Connection conn = null;
PreparedStatement pstmt = null;
ResultSet rs = null;
Class.forName("com.mysql.jdbc.Driver");
String send_id = request.getParameter("send_id");
String dbid = null;
String dbpw = null;
String dblevel = null;
String dbname = null;
String dbemail = null;
String dbphone = null;
String dbaddr = null;
try{
	String jdbcDriver = "jdbc:mysql://localhost:3306/db08kjb?" +
			"useUnicode=true&characterEncoding=euckr";
	String dbUser = "dbid08kjb";
	String dbPass = "dbpw08kjb";
	conn = DriverManager.getConnection(jdbcDriver, dbUser, dbPass);
	System.out.println(conn + "<-- conn");
	pstmt = conn.prepareStatement("SELECT * FROM tb_user WHERE u_id=?");
	pstmt.setString(1, send_id);
	System.out.println(pstmt + "<-- pstmt");
	rs = pstmt.executeQuery();
	System.out.println(rs + "<-- rs ");
	if(rs.next()){
		System.out.println("1-1 if조건문-true-쿼리실행결과 한줄(한명의 회원조회)이 있다.");
		//수정화면 출력 1번 방법 가능
		dbid = rs.getString("u_id");
		dbpw = rs.getString("u_pw");
		dblevel = rs.getString("u_level");
		dbname = rs.getString("u_name");
		dbemail = rs.getString("u_email");
		dbphone = rs.getString("u_phone");
		dbaddr = rs.getString("u_addr");
		System.out.println(dbid + "<- dbid ");
		System.out.println(dbpw + "<- dbpw ");
		System.out.println(dblevel + "<- dblevel ");
		System.out.println(dbname + "<- dbname ");
		System.out.println(dbemail + "<- dbemail ");
		System.out.println(dbphone + "<- dbphone ");
		System.out.println(dbaddr + "<- dbaddr ");
	}else{
		System.out.println("1-2 if조건문-false-쿼리실행결과 없다.");
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
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=EUC-KR">
<title>Insert title here</title>
<!-- <link rel="stylesheet" type="text/css" href="/layoutMG/css/main.css" /> -->
<link rel="stylesheet" type="text/css" href="<%= request.getContextPath() %>/css/main2.css" />
</head>

<body>
<%@ include file="/module/top.jsp" %>
<%@ include file="/module/left.jsp" %>
<form action="<%= request.getContextPath() %>/uupdate/u_update_action.jsp" method="post">
<table border="1">
<tr>
	<td>아이디</td>
	<td><input type="text" name="u_id" size="20" readonly value="<%= dbid %>"></td>
<tr>
<tr>
	<td>암호</td>
	<td><input type="text" name="u_pw" size="20" value="<%= dbpw %>"></td>
<tr>
<tr>
	<td>권한</td>
	<td><input type="text" name="u_level" size="20" value="<%= dblevel %>"></td>
<tr>
<tr>
	<td>이름</td>
	<td><input type="text" name="u_name" size="20" value="<%= dbname %>"></td>
<tr>
<tr>
	<td>이메일</td>
	<td><input type="text" name="u_email" size="20" value="<%= dbemail %>"></td>
<tr>
<tr>
	<td>휴대폰</td>
	<td><input type="text" name="u_phone" size="20" value="<%= dbphone %>"></td>
<tr>
<tr>
	<td>주소</td>
	<td><input type="text" name="u_addr" size="20" value="<%= dbaddr %>"></td>
<tr>
<tr>
	<td colspan="4"><input type="submit" value="수정버튼"></td>
</tr>
</table>
</form>
<%@ include file="/module/hadan.jsp" %>

</body>
</html>

