/*
 * Generated by the Jasper component of Apache Tomcat
 * Version: Apache Tomcat/10.0.23
 * Generated at: 2022-10-04 12:06:00 UTC
 * Note: The last modified time of this file was set to
 *       the last modified time of the source file after
 *       generation to assist with modification tracking.
 */
package org.apache.jsp.minsert;

import jakarta.servlet.*;
import jakarta.servlet.http.*;
import jakarta.servlet.jsp.*;

public final class m_005finsert_005fform_jsp extends org.apache.jasper.runtime.HttpJspBase
    implements org.apache.jasper.runtime.JspSourceDependent,
                 org.apache.jasper.runtime.JspSourceImports {

  private static final jakarta.servlet.jsp.JspFactory _jspxFactory =
          jakarta.servlet.jsp.JspFactory.getDefaultFactory();

  private static java.util.Map<java.lang.String,java.lang.Long> _jspx_dependants;

  static {
    _jspx_dependants = new java.util.HashMap<java.lang.String,java.lang.Long>(3);
    _jspx_dependants.put("/module/hadan.jsp", Long.valueOf(1664883680796L));
    _jspx_dependants.put("/module/left.jsp", Long.valueOf(1664883680790L));
    _jspx_dependants.put("/module/top.jsp", Long.valueOf(1664885154826L));
  }

  private static final java.util.Set<java.lang.String> _jspx_imports_packages;

  private static final java.util.Set<java.lang.String> _jspx_imports_classes;

  static {
    _jspx_imports_packages = new java.util.HashSet<>();
    _jspx_imports_packages.add("jakarta.servlet");
    _jspx_imports_packages.add("jakarta.servlet.http");
    _jspx_imports_packages.add("jakarta.servlet.jsp");
    _jspx_imports_classes = null;
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
      out.write("<html>\r\n");
      out.write("<head>\r\n");
      out.write("<meta charset=\"EUC-KR\">\r\n");
      out.write("<title>Insert title here</title>\r\n");
      out.write("<!-- 상대경로 방법 -->\r\n");
      out.write("<!-- <link rel=\"stylesheet\" type=\"text/css\" href=\"./css/main.css\" /> -->\r\n");
      out.write("<!-- 절대경로 방법1 : 문제점 : 프로젝트명 변경되면 망했다. 왜? 관련 1억개 파일 변경 -->\r\n");
      out.write("<!-- <link rel=\"stylesheet\" type=\"text/css\" href=\"/layoutMG45/css/main.css\" /> -->\r\n");
      out.write("<!-- 절대경로 방법2 -->\r\n");
      out.write("<link rel=\"stylesheet\" type=\"text/css\" href=\"");
      out.print( request.getContextPath() );
      out.write("/css/main.css\" />\r\n");
      out.write("</head>\r\n");
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
      out.write("/user/user_insert_form.jsp\">01회원등록</a><br/>	       		 \r\n");
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
      out.write("\r\n");
      out.write("\r\n");
      out.write("<form action=\"");
      out.print( request.getContextPath() );
      out.write("/minsert/m_insert_action.jsp\" method=\"post\">\r\n");
      out.write("<table border=\"1\">\r\n");
      out.write("<tr>\r\n");
      out.write("	<td>아이디</td>\r\n");
      out.write("	<td><input type=\"text\" name=\"m_id\" size=\"20\"></td>\r\n");
      out.write("<tr>\r\n");
      out.write("<tr>\r\n");
      out.write("	<td>암호</td>\r\n");
      out.write("	<td><input type=\"text\" name=\"m_pw\" size=\"20\"></td>\r\n");
      out.write("<tr>\r\n");
      out.write("<tr>\r\n");
      out.write("	<td>권한</td>\r\n");
      out.write("	<td><input type=\"text\" name=\"m_level\" size=\"20\"></td>\r\n");
      out.write("<tr>\r\n");
      out.write("<tr>\r\n");
      out.write("	<td>이름</td>\r\n");
      out.write("	<td><input type=\"text\" name=\"m_name\" size=\"20\"></td>\r\n");
      out.write("<tr>\r\n");
      out.write("<tr>\r\n");
      out.write("	<td>이메일</td>\r\n");
      out.write("	<td><input type=\"text\" name=\"m_email\" size=\"20\"></td>\r\n");
      out.write("<tr>\r\n");
      out.write("<tr>\r\n");
      out.write("	<td colspan=\"4\"><input type=\"submit\" value=\"회원가입버튼\"></td>\r\n");
      out.write("</tr>\r\n");
      out.write("</table>\r\n");
      out.write("</form>\r\n");
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
      out.write("</body>\r\n");
      out.write("</html>\r\n");
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
