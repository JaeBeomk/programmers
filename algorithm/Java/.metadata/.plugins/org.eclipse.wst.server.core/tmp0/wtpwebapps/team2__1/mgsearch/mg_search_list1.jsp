<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<%@ page import = "java.sql.DriverManager" %>
<%@ page import = "java.sql.Connection" %>
<%@ page import = "java.sql.PreparedStatement" %>
<%@ page import = "java.sql.ResultSet" %>
<%@ page import = "java.sql.SQLException" %>
<%@ page import="kr.or.ksmart.driverdb.DriverDB" %>

<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=EUC-KR">
<title>Insert title here</title>
<!-- <link rel="stylesheet" type="text/css" href="/layoutMG/css/main.css" /> -->
<link rel="stylesheet" type="text/css" href="<%= request.getContextPath() %>/css/main.css" />
<style>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>
</head>

<body>
<%@ include file="/module/top.jsp" %>
<%@ include file="/module/left.jsp" %>
<%@ include file="/mgsearch/mg_search_form1.jsp" %>
��ǰ ����Ʈ(ȸ�����̺��� join�˻�1) <br>
<table width="100%" border="1">
<tr>
   <td>���̵�</td><td>�̸�</td><td>��ǰ�ڵ�</td><td>��ǰ��</td><td>�з�</td><td>����</td><td>����</td><td>������</td><td>�����</td><td>��</td><td>����</td><td>����</td>
</tr>
<%
request.setCharacterEncoding("euc-kr");   //post�ѱ�ó��
String sk = request.getParameter("sk");
String sv = request.getParameter("sv");
String start_date = request.getParameter("start_date");
String end_date = request.getParameter("end_date");
System.out.println(sk + "<- sk ");
System.out.println(sv + "<- sv ");
System.out.println(start_date + "<- start_date ");
System.out.println(end_date + "<- end_date ");
Connection conn = null;
PreparedStatement pstmt = null;
ResultSet rs = null;
String selectQuery1="select tb_member.*, tb_goods.* " +
"from tb_member inner join tb_goods on tb_member.m_id = tb_goods.m_id";

String selectQuery2="select tb_member.*, tb_goods.* " +
"from tb_member inner join tb_goods on tb_member.m_id = tb_goods.m_id "+ 
"and DATE_FORMAT(g_date,'%Y-%m-%d') between ? and ?";


try{
	DriverDB db = new DriverDB();
	conn = db.driverDbcon();

   System.out.println(conn + "<-- conn ");
   
   if(start_date==null && end_date == null && sk==null && sv==null){
      pstmt = conn.prepareStatement(selectQuery1);
      
   }else if(start_date.equals("") && sv.equals("")){
	   pstmt = conn.prepareStatement(selectQuery1);
   }else if(start_date.equals("")){
	   if(sk.equals("g_name")){
		   pstmt = conn.prepareStatement(selectQuery1 +" where tb_goods."+sk+" LIKE '%"+sv+"%' order by g_date");
	   }else{
		   pstmt = conn.prepareStatement(selectQuery1 +" where tb_goods."+sk+"=? order by g_date");
		   pstmt.setString(1, sv); 
	   }
   }else{
	   if(sv.equals("")){
		   pstmt = conn.prepareStatement(selectQuery2 + "order by g_date");
		   pstmt.setString(1, start_date);
		   pstmt.setString(2, end_date);  
	   }else{
		   if(sk.equals("g_name")){
			   pstmt = conn.prepareStatement(selectQuery2 +" where tb_goods."+sk+" LIKE '%"+sv+"%' order by g_date");
			   pstmt.setString(1, start_date);
			   pstmt.setString(2, end_date); 
		   }else{
		   pstmt = conn.prepareStatement(selectQuery2 +" where tb_goods."+sk+"=? order by g_date");

		   pstmt.setString(1, start_date);
		   pstmt.setString(2, end_date); 
		   pstmt.setString(3, sv); 
		   }
	   }
   }
   
   System.out.println(pstmt + "<-- pstmt");
//�������� �غ� �ܰ� : �پ��� ���ǹ��� �ۼ� �ϸ� ��!~~~~~~~~~~~   

   rs = pstmt.executeQuery();
   System.out.println(rs + "<-- rs m_search_form.jsp");
   //System.out.println(rs.next() + "<-- rs.next() m_search_form.jsp");
   while(rs.next()){
      System.out.println("while �ݺ� Ƚ��");
%>      
      
      <tr>
      <td><%= rs.getString("m_id")%></td>
      <td><%= rs.getString("m_name")%></td>
      
      <td><%= rs.getString("g_code")%></td>
      <td><%= rs.getString("g_name")%></td>
      <td><%= rs.getString("g_cate")%></td>
      <td><%= rs.getString("g_price")%></td>
      <td><%= rs.getString("g_color")%></td>
      <td><%= rs.getString("g_size")%></td>
      <td><%= rs.getString("g_date")%></td>
      <td><%= rs.getString("g_desc")%></td>
      <td>
<a href="<%= request.getContextPath() %>/mgupdate/mg_update_form.jsp?g_code=<%= rs.getString("g_code")%>">������ư</a>         
      </td>
      <td>
<a href="<%= request.getContextPath() %>/mgdelete/mg_delete_action.jsp?g_code=<%= rs.getString("g_code")%>">������ư</a>         
      </td>
   </tr>         
<%      
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
</table>          
<%@ include file="/module/hadan.jsp" %>

</body>
</html>