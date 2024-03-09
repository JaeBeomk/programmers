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

//select 쿼리 실행 결과 값들을 담기 위한 변수 선언
try{
	DriverDB db = new DriverDB();
	conn = db.driverDbcon();
	String select1="select1 : "+request.getParameter("select")+"번";
	pstmt = conn.prepareStatement("SELECT * FROM tb_goods WHERE g_code=?");
	pstmt.setString(1, g_code);
	System.out.println(pstmt + "<-- pstmt");
	rs = pstmt.executeQuery();
	System.out.println(rs + "<-- rs mg_update_form.jsp");
	//System.out.println(rs.next() + "<-- rs.next() m_update_form.jsp");
	if(rs.next()){
		System.out.println("1-1 쿼리 실행 결과 1줄 있다.");

//1번 방법 : 수정화면 출력 할 수 있다.		
		dbcode = rs.getString("g_code");
		dbid = rs.getString("m_id");
		dbname = rs.getString("g_name");
		dbcate = rs.getString("g_cate");
		dbprice = rs.getString("g_price");
		dbcolor = rs.getString("g_color");
		dbsize = rs.getString("g_size");
		dbdesc = rs.getString("g_desc");
		
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
<form action="<%= request.getContextPath() %>/mgupdate/mg_update_action.jsp" method="post">

<table border="1">
<input type="hidden" name="m_id" value="<%= S_ID %>">
<tr>
	<td>상품코드</td>
	<td><input type="text" name="g_code" size="20" value="<%= dbcode %>" readonly></td>
<tr>
<tr>
	<td>판매자 아이디</td>
	<td><input type="text" name="m_id" size="20" value="<%= dbid %>"></td>
<tr>
<tr>
	<td>상품명</td> 
	<td> <input type="text" name="g_name" value="<%= dbname %>"> </td>
</tr>
<tr>
	<td>카테고리 </td> 
	<td><select name="g_cate" >
		<option value="가방">가방</option>
		<option value="신발">신발</option>
	</select></td>
</tr>
<tr>
	<td>가격 </td>
	<td> <input type="text" name="g_price" value="<%= dbprice %>"> </td>
</tr>
<tr>
	<td>색상 </td>
	<td> 
	<select name="g_color">
		<option value="black">블랙</option>
		<option value="brown">브라운</option>
		<option value="red">레드</option>
		<option value="white">화이트</option>
	</select> 
	</td>
</tr>
<tr>
	<td>사이즈</td>
	<td> 
	<select name="g_size" >
		<option value="S">S</option>
		<option value="M">M</option>
		<option value="L">L</option>
	</select> 
	</td>
</tr>
<tr>
	<td>상세</td>
	<td> <input type="text" name="g_desc" value="<%= dbdesc %>"></td>
</tr>
<tr>
	<td>
	<input type="submit" value="상품수정버튼">
	</td>
</tr>
</table>
</form>
<%@ include file="/module/hadan.jsp" %>
</body>
</html>