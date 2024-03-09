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
//select 쿼리 실행 결과 값들을 담기 위한 변수 선언
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











<!-- 
m_list.jsp
1) 수정버튼 클릭시에 get방식으로 아이디 값을 넘긴다
m_update_form.jsp
2) 아이디 값을 받아서 콘솔창에 확인한다
3) 드라이버로딩 4) DB연결
5) 쿼리실행 준비 SELECT * FROM tb_member WHERE m_id=?
SELECT * FROM tb_member WHERE m_id='id002' <-- 쿼리문장 완성
6) 쿼리 실행 
7) 쿼리실행결과 ( 수정 화면에 뿌려준다 ) : 
 첫번째 처리과정에 수정화면을 뿌리는 방식 / 두번째 수정 화면 별도로 구성하고 값을 뿌리도록 해보자!
8)9)10) 객체종료
-->