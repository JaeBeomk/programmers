/*
 * Generated by the Jasper component of Apache Tomcat
 * Version: Apache Tomcat/10.0.23
 * Generated at: 2022-10-12 14:27:55 UTC
 * Note: The last modified time of this file was set to
 *       the last modified time of the source file after
 *       generation to assist with modification tracking.
 */
package org.apache.jsp.mgsearch;

import jakarta.servlet.*;
import jakarta.servlet.http.*;
import jakarta.servlet.jsp.*;
import java.sql.DriverManager;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import kr.or.ksmart.driverdb.DriverDB;

public final class mg_005fsearch_005flist1_jsp extends org.apache.jasper.runtime.HttpJspBase
    implements org.apache.jasper.runtime.JspSourceDependent,
                 org.apache.jasper.runtime.JspSourceImports {

  private static final jakarta.servlet.jsp.JspFactory _jspxFactory =
          jakarta.servlet.jsp.JspFactory.getDefaultFactory();

  private static java.util.Map<java.lang.String,java.lang.Long> _jspx_dependants;

  static {
    _jspx_dependants = new java.util.HashMap<java.lang.String,java.lang.Long>(4);
    _jspx_dependants.put("/module/hadan.jsp", Long.valueOf(1665577584675L));
    _jspx_dependants.put("/module/left.jsp", Long.valueOf(1665577584670L));
    _jspx_dependants.put("/module/top.jsp", Long.valueOf(1665580201930L));
    _jspx_dependants.put("/mgsearch/mg_search_form1.jsp", Long.valueOf(1665577584649L));
  }

  private static final java.util.Set<java.lang.String> _jspx_imports_packages;

  private static final java.util.Set<java.lang.String> _jspx_imports_classes;

  static {
    _jspx_imports_packages = new java.util.HashSet<>();
    _jspx_imports_packages.add("jakarta.servlet");
    _jspx_imports_packages.add("jakarta.servlet.http");
    _jspx_imports_packages.add("jakarta.servlet.jsp");
    _jspx_imports_classes = new java.util.HashSet<>();
    _jspx_imports_classes.add("java.sql.SQLException");
    _jspx_imports_classes.add("java.sql.Connection");
    _jspx_imports_classes.add("kr.or.ksmart.driverdb.DriverDB");
    _jspx_imports_classes.add("java.sql.ResultSet");
    _jspx_imports_classes.add("java.sql.PreparedStatement");
    _jspx_imports_classes.add("java.sql.DriverManager");
  }

  private volatile jakarta.el.ExpressionFactory _el_expressionfactory;
  private volatile org.apache.tomcat.InstanceManager _jsp_instancemanager;

  public java.util.Map<java.lang.String,java.lang.Long> getDependants() {
    return _jspx_dependants;
  }

  public java.util.Set<java.lang.String> getPackageImports() {
    return _jspx_imports_packages;
  }

  public java.util.Set<java.lang.String> getClassImports() {
    return _jspx_imports_classes;
  }

  public jakarta.el.ExpressionFactory _jsp_getExpressionFactory() {
    if (_el_expressionfactory == null) {
      synchronized (this) {
        if (_el_expressionfactory == null) {
          _el_expressionfactory = _jspxFactory.getJspApplicationContext(getServletConfig().getServletContext()).getExpressionFactory();
        }
      }
    }
    return _el_expressionfactory;
  }

  public org.apache.tomcat.InstanceManager _jsp_getInstanceManager() {
    if (_jsp_instancemanager == null) {
      synchronized (this) {
        if (_jsp_instancemanager == null) {
          _jsp_instancemanager = org.apache.jasper.runtime.InstanceManagerFactory.getInstanceManager(getServletConfig());
        }
      }
    }
    return _jsp_instancemanager;
  }

  public void _jspInit() {
  }

  public void _jspDestroy() {
  }

  public void _jspService(final jakarta.servlet.http.HttpServletRequest request, final jakarta.servlet.http.HttpServletResponse response)
      throws java.io.IOException, jakarta.servlet.ServletException {

    if (!jakarta.servlet.DispatcherType.ERROR.equals(request.getDispatcherType())) {
      final java.lang.String _jspx_method = request.getMethod();
      if ("OPTIONS".equals(_jspx_method)) {
        response.setHeader("Allow","GET, HEAD, POST, OPTIONS");
        return;
      }
      if (!"GET".equals(_jspx_method) && !"POST".equals(_jspx_method) && !"HEAD".equals(_jspx_method)) {
        response.setHeader("Allow","GET, HEAD, POST, OPTIONS");
        response.sendError(HttpServletResponse.SC_METHOD_NOT_ALLOWED, "JSP들은 오직 GET, POST 또는 HEAD 메소드만을 허용합니다. Jasper는 OPTIONS 메소드 또한 허용합니다.");
        return;
      }
    }

    final jakarta.servlet.jsp.PageContext pageContext;
    jakarta.servlet.http.HttpSession session = null;
    final jakarta.servlet.ServletContext application;
    final jakarta.servlet.ServletConfig config;
    jakarta.servlet.jsp.JspWriter out = null;
    final java.lang.Object page = this;
    jakarta.servlet.jsp.JspWriter _jspx_out = null;
    jakarta.servlet.jsp.PageContext _jspx_page_context = null;


    try {
      response.setContentType("text/html; charset=EUC-KR");
      pageContext = _jspxFactory.getPageContext(this, request, response,
      			null, true, 8192, true);
      _jspx_page_context = pageContext;
      application = pageContext.getServletContext();
      config = pageContext.getServletConfig();
      session = pageContext.getSession();
      out = pageContext.getOut();
      _jspx_out = out;

      out.write("\r\n");
      out.write("<!DOCTYPE html PUBLIC \"-//W3C//DTD HTML 4.01 Transitional//EN\" \"http://www.w3.org/TR/html4/loose.dtd\">\r\n");
      out.write("\r\n");
      out.write("\r\n");
      out.write("\r\n");
      out.write("\r\n");
      out.write("\r\n");
      out.write("\r\n");
      out.write("\r\n");
      out.write("<html>\r\n");
      out.write("<head>\r\n");
      out.write("<meta http-equiv=\"Content-Type\" content=\"text/html; charset=EUC-KR\">\r\n");
      out.write("<title>Insert title here</title>\r\n");
      out.write("<!-- <link rel=\"stylesheet\" type=\"text/css\" href=\"/layoutMG/css/main.css\" /> -->\r\n");
      out.write("<link rel=\"stylesheet\" type=\"text/css\" href=\"");
      out.print( request.getContextPath() );
      out.write("/css/main.css\" />\r\n");
      out.write("<style>\r\n");
      out.write("table {\r\n");
      out.write("  font-family: arial, sans-serif;\r\n");
      out.write("  border-collapse: collapse;\r\n");
      out.write("  width: 100%;\r\n");
      out.write("}\r\n");
      out.write("\r\n");
      out.write("td, th {\r\n");
      out.write("  border: 1px solid #dddddd;\r\n");
      out.write("  text-align: left;\r\n");
      out.write("  padding: 8px;\r\n");
      out.write("}\r\n");
      out.write("\r\n");
      out.write("tr:nth-child(even) {\r\n");
      out.write("  background-color: #dddddd;\r\n");
      out.write("}\r\n");
      out.write("</style>\r\n");
      out.write("</head>\r\n");
      out.write("\r\n");
      out.write("<body>\r\n");
      out.write("\r\n");
      out.write("<!DOCTYPE html>\r\n");

System.out.println(session + "<- session top.jsp");
System.out.println(request + "<- request top.jsp");
System.out.println(response + "<- response top.jsp");
System.out.println(out + "<- out top.jsp");
String S_ID = (String)session.getAttribute("S_ID");
String S_NAME = (String)session.getAttribute("S_NAME");
String S_LEVEL = (String)session.getAttribute("S_LEVEL");
System.out.println(S_ID + "<- S_ID top.jsp");
System.out.println(S_NAME + "<- S_NAME top.jsp");
System.out.println(S_LEVEL + "<- S_LEVEL top.jsp");

      out.write("\r\n");
      out.write("   <!-- Begin Wrapper -->\r\n");
      out.write("   <div id=\"wrapper\">\r\n");
      out.write("   \r\n");
      out.write("         <!-- Begin Header -->\r\n");
      out.write("         <div id=\"header\">\r\n");
      out.write("         /module/top.jsp	<br/>\r\n");
      out.write("		       상단 메뉴	<br/><br/>\r\n");

if(S_LEVEL == null){

      out.write("		\r\n");
      out.write("<!-- 1 로그인 전 화면 시작 -->	\r\n");
      out.write("<a href=\"");
      out.print( request.getContextPath() );
      out.write("/minsert/m_insert_form.jsp\">01회원등록</a><br/>	       		 \r\n");
      out.write("<form action=\"");
      out.print( request.getContextPath() );
      out.write("/login/login_action.jsp\" method=\"post\">\r\n");
      out.write("	아이디:	<input type=\"text\" name=\"id\">\r\n");
      out.write("	비번 : <input type=\"text\" name=\"pw\">\r\n");
      out.write("	<input type=\"submit\" value=\"로그인버튼\"> \r\n");
      out.write("</form> \r\n");
      out.write("<!-- 1 로그인 전 화면 끝 -->\r\n");

}else{
	if(S_LEVEL.equals("구매자")){

      out.write("		\r\n");
      out.write("<a href=\"");
      out.print( request.getContextPath() );
      out.write("/minsert/m_insert_form.jsp\">01회원등록</a>\r\n");
      out.write("<a href=\"#\">04상품검색</a>	<br/>	\r\n");
		
	}else if(S_LEVEL.equals("판매자")){

      out.write("		\r\n");
      out.write("<a href=\"");
      out.print( request.getContextPath() );
      out.write("/minsert/m_insert_form.jsp\">01회원등록</a>\r\n");
      out.write("<a href=\"");
      out.print( request.getContextPath() );
      out.write("/mginsert/goods_insert_form2.jsp\">03상품등록</a>\r\n");
      out.write("<a href=\"");
      out.print( request.getContextPath() );
      out.write("/mgsearch/mg_search_list1.jsp\">04상품검색</a>		\r\n");
      out.write("<a href=\"");
      out.print( request.getContextPath() );
      out.write("/mgsearch/mg_search_list1.jsp\">05상품회원join검색1</a>	<br/>	\r\n");
		
	}else if(S_LEVEL.equals("관리자")){

      out.write("		\r\n");
      out.write("<a href=\"");
      out.print( request.getContextPath() );
      out.write("/minsert/m_insert_form.jsp\">01회원등록</a>\r\n");
      out.write("<a href=\"");
      out.print( request.getContextPath() );
      out.write("/msearch/m_search_list.jsp\">02회원검색</a>\r\n");
      out.write("<a href=\"");
      out.print( request.getContextPath() );
      out.write("/mginsert/goods_insert_form2.jsp\">03상품등록</a>\r\n");
      out.write("<a href=\"");
      out.print( request.getContextPath() );
      out.write("/mgsearch/mg_search_list1.jsp\">04상품검색</a>	\r\n");
      out.write("<a href=\"");
      out.print( request.getContextPath() );
      out.write("/mgsearch/mg_search_list1.jsp\">05상품회원join검색1</a>	<br/>	\r\n");
      out.write("\r\n");
		
	}

      out.write("\r\n");
      out.write("<!-- 2 로그인 후 화면 시작 -->\r\n");
      out.write("	");
      out.print( S_NAME );
      out.write(' ');
      out.write('님');
      out.write(' ');
      out.print( S_LEVEL );
      out.write(" 권한 로그인 상태\r\n");
      out.write("<a href=\"");
      out.print( request.getContextPath() );
      out.write("/login/logout.jsp\">로그아웃</a>\r\n");
      out.write("<!-- 2 로그인 후 화면 끝 -->\r\n");

}

      out.write("			   \r\n");
      out.write("		 </div>\r\n");
      out.write("		 <!-- End Header -->");
      out.write('\r');
      out.write('\n');
      out.write("\r\n");
      out.write("<!DOCTYPE html>\r\n");
      out.write("		 <!-- Begin Left Column -->\r\n");
      out.write("		 <div id=\"leftcolumn\">\r\n");
      out.write("		 /module/left.jsp	<br/>\r\n");
      out.write("		       왼쪽 메뉴\r\n");
      out.write("		 \r\n");
      out.write("		 </div>\r\n");
      out.write("		 <!-- End Left Column -->\r\n");
      out.write("		 		 <!-- Begin Right Column -->\r\n");
      out.write("		 <div id=\"rightcolumn\">");
      out.write('\r');
      out.write('\n');
      out.write("\r\n");
      out.write("<!DOCTYPE html PUBLIC \"-//W3C//DTD HTML 4.01 Transitional//EN\" \"http://www.w3.org/TR/html4/loose.dtd\">\r\n");
      out.write("\r\n");
      out.write("<form action=\"");
      out.print(request.getContextPath());
      out.write("/mgsearch/mg_search_list1.jsp\" method=\"post\">\r\n");
      out.write("\r\n");
      out.write("<select name=\"sk\">\r\n");
      out.write("	<option value=\"g_code\">상품코드</option>\r\n");
      out.write("	<option value=\"m_id\">판매자아이디</option>\r\n");
      out.write("	<option value=\"g_name\">상품명</option>\r\n");
      out.write("	<option value=\"g_cate\">카테고리</option>\r\n");
      out.write("	<option value=\"g_color\">색상</option>\r\n");
      out.write("	<option value=\"g_size\">사이즈</option>\r\n");
      out.write("</select>\r\n");
      out.write("<input type=\"text\" name=\"sv\">\r\n");
      out.write("<input type=\"date\" name=\"start_date\">\r\n");
      out.write("<input type=\"date\" name=\"end_date\">\r\n");
      out.write("<input type=\"submit\" value=\"검색버튼\">\r\n");
      out.write("</form>");
      out.write("\r\n");
      out.write("상품 리스트(회원테이블과 join검색1) <br>\r\n");
      out.write("<table width=\"100%\" border=\"1\">\r\n");
      out.write("<tr>\r\n");
      out.write("   <td>아이디</td><td>이름</td><td>상품코드</td><td>상품명</td><td>분류</td><td>가격</td><td>색상</td><td>사이즈</td><td>등록일</td><td>상세</td><td>수정</td><td>삭제</td>\r\n");
      out.write("</tr>\r\n");

request.setCharacterEncoding("euc-kr");   //post한글처리
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
//쿼리실행 준비 단계 : 다양한 조건문을 작성 하면 끝!~~~~~~~~~~~   

   rs = pstmt.executeQuery();
   System.out.println(rs + "<-- rs m_search_form.jsp");
   //System.out.println(rs.next() + "<-- rs.next() m_search_form.jsp");
   while(rs.next()){
      System.out.println("while 반복 횟수");

      out.write("      \r\n");
      out.write("      \r\n");
      out.write("      <tr>\r\n");
      out.write("      <td>");
      out.print( rs.getString("m_id"));
      out.write("</td>\r\n");
      out.write("      <td>");
      out.print( rs.getString("m_name"));
      out.write("</td>\r\n");
      out.write("      \r\n");
      out.write("      <td>");
      out.print( rs.getString("g_code"));
      out.write("</td>\r\n");
      out.write("      <td>");
      out.print( rs.getString("g_name"));
      out.write("</td>\r\n");
      out.write("      <td>");
      out.print( rs.getString("g_cate"));
      out.write("</td>\r\n");
      out.write("      <td>");
      out.print( rs.getString("g_price"));
      out.write("</td>\r\n");
      out.write("      <td>");
      out.print( rs.getString("g_color"));
      out.write("</td>\r\n");
      out.write("      <td>");
      out.print( rs.getString("g_size"));
      out.write("</td>\r\n");
      out.write("      <td>");
      out.print( rs.getString("g_date"));
      out.write("</td>\r\n");
      out.write("      <td>");
      out.print( rs.getString("g_desc"));
      out.write("</td>\r\n");
      out.write("      <td>\r\n");
      out.write("<a href=\"");
      out.print( request.getContextPath() );
      out.write("/mgupdate/mg_update_form.jsp?g_code=");
      out.print( rs.getString("g_code"));
      out.write("\">수정버튼</a>         \r\n");
      out.write("      </td>\r\n");
      out.write("      <td>\r\n");
      out.write("<a href=\"");
      out.print( request.getContextPath() );
      out.write("/mgdelete/mg_delete_action.jsp?g_code=");
      out.print( rs.getString("g_code"));
      out.write("\">삭제버튼</a>         \r\n");
      out.write("      </td>\r\n");
      out.write("   </tr>         \r\n");
      
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

      out.write("\r\n");
      out.write("</table>          \r\n");
      out.write("\r\n");
      out.write("<!DOCTYPE html>\r\n");
      out.write("		 </div>\r\n");
      out.write("		 <!-- End Right Column -->\r\n");
      out.write("		 \r\n");
      out.write("		 <!-- Begin Footer -->\r\n");
      out.write("		 <div id=\"footer\">\r\n");
      out.write("		 /module/hadan.jsp	<br/>\r\n");
      out.write("			   한국스마트정보교육원 063-717-1008 ksmart.or.kr		\r\n");
      out.write("	     </div>\r\n");
      out.write("		 <!-- End Footer -->\r\n");
      out.write("		 \r\n");
      out.write("   </div>\r\n");
      out.write("   <!-- End Wrapper -->");
      out.write("\r\n");
      out.write("\r\n");
      out.write("</body>\r\n");
      out.write("</html>");
    } catch (java.lang.Throwable t) {
      if (!(t instanceof jakarta.servlet.jsp.SkipPageException)){
        out = _jspx_out;
        if (out != null && out.getBufferSize() != 0)
          try {
            if (response.isCommitted()) {
              out.flush();
            } else {
              out.clearBuffer();
            }
          } catch (java.io.IOException e) {}
        if (_jspx_page_context != null) _jspx_page_context.handlePageException(t);
        else throw new ServletException(t);
      }
    } finally {
      _jspxFactory.releasePageContext(_jspx_page_context);
    }
  }
}