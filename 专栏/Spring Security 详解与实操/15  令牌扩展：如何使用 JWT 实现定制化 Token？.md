<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>15  令牌扩展：如何使用 JWT 实现定制化 Token？.md</title>
        <!-- Spectre.css framework -->
        <link rel="stylesheet" href="../../static/index.css">
        <!-- theme css & js -->
        <meta name="generator" content="Hexo 4.2.0">
    </head>

<body>

<div class="book-container">
    <div class="book-sidebar">
        <div class="book-brand">
            <a href="../../index.html">
                <img src="../../static/favicon.png">
                <span>技术文章摘抄</span>
            </a>
        </div>
        <div class="book-menu uncollapsible">
            <ul class="uncollapsible">
                <li><a href="../../index.html" class="current-tab">首页</a></li>
            </ul>

            <ul class="uncollapsible">
                <li><a href="../index.html">上一级</a></li>
            </ul>

            <ul class="uncollapsible">
                <li>

                    
                    <a href="00&#32;开篇词&#32;&#32;Spring&#32;Security，为你的应用安全与职业之路保驾护航.md">00 开篇词  Spring Security，为你的应用安全与职业之路保驾护航.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;&#32;顶级框架：Spring&#32;Security&#32;是一款什么样的安全性框架？.md">01  顶级框架：Spring Security 是一款什么样的安全性框架？.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;&#32;用户认证：如何使用&#32;Spring&#32;Security&#32;构建用户认证体系？.md">02  用户认证：如何使用 Spring Security 构建用户认证体系？.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;&#32;认证体系：如何深入理解&#32;Spring&#32;Security&#32;用户认证机制？.md">03  认证体系：如何深入理解 Spring Security 用户认证机制？.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;&#32;密码安全：Spring&#32;Security&#32;中包含哪些加解密技术？.md">04  密码安全：Spring Security 中包含哪些加解密技术？.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;&#32;访问授权：如何对请求的安全访问过程进行有效配置？.md">05  访问授权：如何对请求的安全访问过程进行有效配置？.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;&#32;权限管理：如何剖析&#32;Spring&#32;Security&#32;的授权原理？.md">06  权限管理：如何剖析 Spring Security 的授权原理？.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;&#32;案例实战：使用&#32;Spring&#32;Security&#32;基础功能保护&#32;Web&#32;应用.md">07  案例实战：使用 Spring Security 基础功能保护 Web 应用.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;&#32;管道过滤：如何基于&#32;Spring&#32;Security&#32;过滤器扩展安全性？.md">08  管道过滤：如何基于 Spring Security 过滤器扩展安全性？.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;&#32;攻击应对：如何实现&#32;CSRF&#32;保护和跨域&#32;CORS？.md">09  攻击应对：如何实现 CSRF 保护和跨域 CORS？.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;&#32;全局方法：如何确保方法级别的安全访问？.md">10  全局方法：如何确保方法级别的安全访问？.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;&#32;案例实战：使用&#32;Spring&#32;Security&#32;高级主题保护&#32;Web&#32;应用.md">11  案例实战：使用 Spring Security 高级主题保护 Web 应用.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;&#32;开放协议：OAuth2&#32;协议解决的是什么问题？.md">12  开放协议：OAuth2 协议解决的是什么问题？.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;&#32;授权体系：如何构建&#32;OAuth2&#32;授权服务器？.md">13  授权体系：如何构建 OAuth2 授权服务器？.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;&#32;资源保护：如何基于&#32;OAuth2&#32;协议配置授权过程？.md">14  资源保护：如何基于 OAuth2 协议配置授权过程？.md</a>

                </li>
                <li>

                    <a class="current-tab" href="15&#32;&#32;令牌扩展：如何使用&#32;JWT&#32;实现定制化&#32;Token？.md">15  令牌扩展：如何使用 JWT 实现定制化 Token？.md</a>
                    

                </li>
                <li>

                    
                    <a href="16&#32;&#32;案例实战：基于&#32;Spring&#32;Security&#32;和&#32;Spring&#32;Cloud&#32;构建微服务安全架构.md">16  案例实战：基于 Spring Security 和 Spring Cloud 构建微服务安全架构.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;&#32;案例实战：基于&#32;Spring&#32;Security&#32;和&#32;OAuth2&#32;实现单点登录.md">17  案例实战：基于 Spring Security 和 OAuth2 实现单点登录.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;&#32;技术趋势：如何为&#32;Spring&#32;Security&#32;添加响应式编程特性？.md">18  技术趋势：如何为 Spring Security 添加响应式编程特性？.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;&#32;测试驱动：如何基于&#32;Spring&#32;Security&#32;测试系统安全性？.md">19  测试驱动：如何基于 Spring Security 测试系统安全性？.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;结束语&#32;&#32;以终为始，Spring&#32;Security&#32;的学习总结.md">20 结束语  以终为始，Spring Security 的学习总结.md</a>

                </li>
            </ul>

        </div>
    </div>

    <div class="sidebar-toggle" onclick="sidebar_toggle()" onmouseover="add_inner()" onmouseleave="remove_inner()">
        <div class="sidebar-toggle-inner"></div>
    </div>

    <script>
        function add_inner() {
            let inner = document.querySelector('.sidebar-toggle-inner')
            inner.classList.add('show')
        }

        function remove_inner() {
            let inner = document.querySelector('.sidebar-toggle-inner')
            inner.classList.remove('show')
        }

        function sidebar_toggle() {
            let sidebar_toggle = document.querySelector('.sidebar-toggle')
            let sidebar = document.querySelector('.book-sidebar')
            let content = document.querySelector('.off-canvas-content')
            if (sidebar_toggle.classList.contains('extend')) { // show
                sidebar_toggle.classList.remove('extend')
                sidebar.classList.remove('hide')
                content.classList.remove('extend')
            } else { // hide
                sidebar_toggle.classList.add('extend')
                sidebar.classList.add('hide')
                content.classList.add('extend')
            }
        }
    </script>

    <div class="off-canvas-content">
        <div class="columns">
            <div class="column col-12 col-lg-12">
                <div class="book-navbar">
                    <!-- For Responsive Layout -->
                    <header class="navbar">
                        <section class="navbar-section">
                            <a onclick="open_sidebar()">
                                <i class="icon icon-menu"></i>
                            </a>
                        </section>
                    </header>
                </div>
                <div class="book-content" style="max-width: 960px; margin: 0 auto;
    overflow-x: auto;
    overflow-y: hidden;">
                    <div class="book-post">
                        <p id="tip" align="center"></p>
                        <div><h1>15  令牌扩展：如何使用 JWT 实现定制化 Token？</h1>
<p>上一讲我们详细介绍了在微服务架构中如何使用 Token 对微服务的访问过程进行权限控制，这里的 Token 是类似“b7c2c7e0-0223-40e2-911d-eff82d125b80”的一种字符串结构。显然，这种格式的 Token 包含的内容应该是很有限的，那么是否有办法实现更为丰富的 Token 呢？答案是肯定的。</p>
<p>事实上，在 OAuth2 协议中并没有明确规定 Token 具体的组成结构，而在现实应用中，我也不太建议你使用上一讲中我们用到的 Token 格式，而是更倾向于采用 JWT。今天我们就基于 JWT 讨论如何实现定制化 Token 这一话题。</p>
<h3>什么是 JWT？</h3>
<p>JWT 的全称是 JSON Web Token，所以它本质上是一种基于 JSON 表示的 Token。<strong>JWT 的设计目标就是为 OAuth2 协议中使用的 Token 提供一种标准结构，所以它经常与 OAuth2 协议集成在一起使用</strong>。</p>
<h4>JWT 的基本结构</h4>
<p>从结构上讲，JWT 本身由三段信息构成：第一段为头部（Header），第二段为有效负载（Payload），第三段为签名（Signature）。如下所示：</p>
<pre><code>header. payload. signature
</code></pre>
<p>从数据格式上来看，以上三个部分的内容都是一个 JSON 对象。在 JWT 中，每一段 JSON 对象都用 Base64 进行编码，编码后的内容用“.”号连接一起，所以 JWT 本质上就是一个字符串。如下所示即为一个 JWT 字符串的示例：</p>
<pre><code>eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL3NwcmluZy5leGFtcGxlLmNvbSIsInN1YiI6Im1haWx0bzpzcHJpbmdAZXhhbXBsZS5jb20iLCJuYmYiOjE2MTU4MTg2NDYsImV4cCI6MTYxNTgyMjI0NiwiaWF0IjoxNjE1ODE4NjQ2LCJqdGkiOiJpZDEyMzQ1NiIsInR5cCI6Imh0dHBzOi8vc3ByaW5nLmV4YW1wbGUuY29tL3JlZ2lzdGVyIn0.Nweh3OPKl-p0PrSNDUQZ9LkJVWxjAP76uQscYJFQr9w
</code></pre>
<p>显然，我们无法从这个经过 Base64 编码的字符串中获取任何有用的信息。业界也存在一些在线生成和解析 JWT 的工具，针对上面这个 JWT 字符串，我们可以通过这些工具获取其包含的原始 JSON 数据，如下所示：</p>
<pre><code>{

 alg: &quot;HS256&quot;,

 typ: &quot;JWT&quot;

}.

{

 iss: &quot;https://spring.example.com&quot;,

 sub: &quot;mailto:<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="324142405b5c5572574a535f425e571c515d5f">[email&#160;protected]</a>&quot;,

 nbf: 1615818646,

 exp: 1615822246,

 iat: 1615818646,

 jti: &quot;id123456&quot;,

 typ: &quot;https://spring.example.com/register&quot;

}.

[signature]
</code></pre>
<p>我们可以清晰地看到一个 JWT 中包含的 Header 部分和 Payload 部分的数据，出于安全考虑，JWT 解析工具通常都不会展示 Signature 部分数据。</p>
<h4>JWT 的优势</h4>
<p>JWT 具有很多优秀的功能特性，它的数据表示方式采用语言无关的 JSON 格式，可以与各个异构系统进行集成。同时，JWT 是一种表示数据的标准，所有人都可以遵循这种标准来传递数据。</p>
<p>在安全领域，我们通常用它<strong>传递被认证的用户身份信息</strong>，以便从资源服务器获取资源。同时，JWT 在结构上也提供了良好的扩展性，开发人员可以根据需求增加一些额外信息用于处理复杂的业务逻辑。因为 JWT 中的数据都是被加密的，所以它除了可以直接用于认证，也可以处理加密需求。</p>
<h3>如何集成 OAuth2 与 JWT？</h3>
<p>看到这里，可能你已经认识到了JWT 和 OAuth2 面向的是不同的应用场景，本身并没有任何关联。但在很多情况下，我们讨论 OAuth2 的实现时，会把 JWT 作为一种认证机制进行使用。</p>
<p>Spring Security 为 JWT 的生成和验证提供了开箱即用的支持。当然，想要发送和消费 JWT，OAuth2 授权服务和各个受保护的微服务必须以不同的方式进行配置。整个开发流程与上一讲介绍的生成普通 Token 是一致的，不同之处在于配置的内容和方式。接下来，我们来看如何在 OAuth2 授权服务器中配置 JWT。</p>
<p>对于所有需要用到 JWT 的独立服务来说，首先我们需要<strong>在 Maven 的 pom 文件中添加对应的依赖包</strong>，如下所示：</p>
<pre><code>&lt;dependency&gt;

&lt;groupId&gt;org.springframework.security&lt;/groupId&gt;

&lt;artifactId&gt;spring-security-jwt&lt;/artifactId&gt;

&lt;/dependency&gt;
</code></pre>
<p>下一步就是提供一个配置类用于完成 JWT 的生成和转换。事实上，在 OAuth2 协议中专门提供了一个接口用于管理 Token 的存储，这个接口就是 TokenStore，而该接口的实现类 JwtTokenStore 则专门用来存储 JWT Token。对应的，我们也将创建一个用于配置 JwtTokenStore 的配置类 JWTTokenStoreConfig，如下所示：</p>
<pre><code>@Configuration

public class JWTTokenStoreConfig {



@Bean

public TokenStore tokenStore() {

return new JwtTokenStore(jwtAccessTokenConverter());

}



@Bean

public JwtAccessTokenConverter jwtAccessTokenConverter() {

JwtAccessTokenConverter converter = new JwtAccessTokenConverter();

converter.setSigningKey(&quot;123456&quot;);

return converter;

}



@Bean

public DefaultTokenServices tokenServices() {

DefaultTokenServices defaultTokenServices = new DefaultTokenServices();

defaultTokenServices.setTokenStore(tokenStore());

defaultTokenServices.setSupportRefreshToken(true);

return defaultTokenServices;

}

}
</code></pre>
<p>可以看到，这里构建了 JwtTokenStore 对象，而在它的构造函数中传入了一个 JwtAccessTokenConverter。JwtAccessTokenConverters 是一个用来转换 JWT 的转换器，转换的过程需要签名键。创建 JwtTokenStore 后，我们通过 tokenServices 方法返回了已经设置 JwtTokenStore 对象的 DefaultTokenServices。</p>
<p>上述 JWTTokenStoreConfig 的作用就是创建了一系列对象以供 Spring 容器使用，我们什么时候会用到这些对象呢？答案就是在将 JWT 集成到 OAuth2 授权服务的过程中，而这个过程似曾相似。基于 13 讲“[授权体系：如何构建 OAuth2 授权服务器？]”中的讨论，我们可以构建一个配置类来覆写 AuthorizationServerConfigurerAdapter 中的 configure 方法，回想原先的这个configure 方法实现如下：</p>
<pre><code>@Override

public void configure(AuthorizationServerEndpointsConfigurer endpoints) throws Exception {

 

        endpoints.authenticationManager(authenticationManager)

                .userDetailsService(userDetailsService);

}
</code></pre>
<p>集成 JWT 之后，该方法的实现过程则需要调整，如下所示：</p>
<pre><code>@Override

public void configure(AuthorizationServerEndpointsConfigurer endpoints) throws Exception {

        TokenEnhancerChain tokenEnhancerChain = new TokenEnhancerChain();

              tokenEnhancerChain.setTokenEnhancers(Arrays.asList(jwtTokenEnhancer, jwtAccessTokenConverter));

        endpoints.tokenStore(tokenStore).accessTokenConverter(jwtAccessTokenConverter).tokenEnhancer(tokenEnhancerChain)

        .authenticationManager(authenticationManager)

        .userDetailsService(userDetailsService);

}
</code></pre>
<p>可以看到，这里构建了一个针对 Token 的增强链 TokenEnhancerChain，并用到了在 JWTTokenStoreConfig 中创建的 tokenStore、jwtAccessTokenConverter 对象。至此，我们在 OAuth2 协议中集成 JWT 的过程就介绍完了，也就是说现在我们访问 OAuth2 授权服务器时获取的 Token 应该就是 JWT Token。</p>
<p>我们来尝试一下，通过 Postman，我们发起了请求并得到了相应的 Token：</p>
<pre><code>{

    &quot;access_token&quot;: &quot;eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzeXN0ZW0iOiJTcHJpbmcgU3lzdGVtIiwidXNlcl9uYW1lIjoic3ByaW5nX3VzZXIiLCJzY29wZSI6WyJ3ZWJjbGllbnQiXSwiZXhwIjoxNjE3NTYwODU0LCJhdXRob3JpdGllcyI6WyJST0xFX1VTRVIiXSwianRpIjoiY2UyYTgzZmYtMjMzMC00YmQ1LTk4MzUtOWIyYzE0N2Y2MTcyIiwiY2xpZW50X2lkIjoic3ByaW5nIn0.Cd_x3r-Fi9hudA2W80amLEga0utPiOJCgBxxLI4Lsb8&quot;,

    &quot;token_type&quot;: &quot;bearer&quot;,

    &quot;refresh_token&quot;: &quot;eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzeXN0ZW0iOiJTcHJpbmcgU3lzdGVtIiwidXNlcl9uYW1lIjoic3ByaW5nX3VzZXIiLCJzY29wZSI6WyJ3ZWJjbGllbnQiXSwiYXRpIjoiY2UyYTgzZmYtMjMzMC00YmQ1LTk4MzUtOWIyYzE0N2Y2MTcyIiwiZXhwIjoxNjIwMTA5NjU0LCJhdXRob3JpdGllcyI6WyJST0xFX1VTRVIiXSwianRpIjoiMDA0NjIxY2MtMmRmZi00ZDJiLWE0YWUtNTU5MzM5YzkyYmFhIiwiY2xpZW50X2lkIjoic3ByaW5nIn0.xDhGwhNTq7Iun9yLENaCvh8mrVHkabu3J8sP0NXENq0&quot;,

    &quot;expires_in&quot;: 43199,

    &quot;scope&quot;: &quot;webclient&quot;,

    &quot;system&quot;: &quot;Spring System&quot;,

    &quot;jti&quot;: &quot;ce2a83ff-2330-4bd5-9835-9b2c147f6172&quot;

}
</code></pre>
<p>显然，这里的 access_token 和 refresh_token 已经是经过 Base64 编码的字符串。同样，我们可以通过在线工具来解析这个 JSON 数据格式的内容，如下所示的就是 access_token 的原始内容：</p>
<pre><code>{

 alg: &quot;HS256&quot;,

 typ: &quot;JWT&quot;

}.

{

 system: &quot;Spring System&quot;,

 user_name: &quot;spring_user&quot;,

 scope: [

  &quot;webclient&quot;

 ],

 exp: 1617560854,

 authorities: [

  &quot;ROLE_USER&quot;

 ],

 jti: &quot;ce2a83ff-2330-4bd5-9835-9b2c147f6172&quot;,

 client_id: &quot;spring&quot;

}.

[signature]
</code></pre>
<h3>如何在微服务中使用 JWT？</h3>
<p>在微服务中使用 JWT 的第一步也是配置工作。我们需要在各个微服务中添加一个 WTTokenStoreConfig 配置类，这个配置类的内容就是创建一个 JwtTokenStore 并构建 tokenServices，具体代码在前面已经做了介绍，这里不再展开。</p>
<p>配置工作完成后，剩下的问题就是在服务调用链中传播 JWT。在上一讲中，我们给出了 OAuth2RestTemplate 这个工具类，该类可以传播普通的 Token。可惜的是，它并不能传播基于 JWT 的 Token。从实现原理上，OAuth2RestTemplate 也是在 RestTemplate 的基础上做了一层封装，所以我们的思路也是尝试<strong>在 RestTemplate 请求中添加对 JWT 的支持</strong>。</p>
<ul>
<li>我们知道， HTTP 请求是通过在 Header 部分中添加一个“Authorization”消息头来完成对 Token 的传递，所以第一步需要能够从 HTTP 请求中获取这个 JWT Token。</li>
<li>然后第二步我们需要将这个 Token 存储在一个线程安全的地方，以便在后续的服务链中进行使用。</li>
<li>第三步，也是最关键的一步，就是在通过 RestTemplate 发起请求时，能够把这个 Token 自动嵌入到所发起的每一个 HTTP 请求中。</li>
</ul>
<p>整个实现思路如下图所示：</p>
<p><img src="assets/Cgp9HWDwBeGACDQUAAFfi6HuFQU869.jpg" alt="1.png" />
在服务调用链中传播 JWT Token 的三个实现步骤</p>
<p>实现这一思路需要你对 HTTP 请求的过程和原理有一定的理解，在代码实现上也需要有一些技巧，下面我一一展开。</p>
<p>首先，在 HTTP 请求过程中，我们可以通过过滤器 Filter 对所有请求进行过滤。Filter 是 Servlet 中的一个核心组件，其基本原理就是构建一个过滤器链并对经过该过滤器链的请求和响应添加定制化的处理机制。Filter 接口的定义如下所示：</p>
<pre><code>public interface Filter {

    public void init(FilterConfig filterConfig) throws ServletException;

    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) throws IOException, ServletException;

    public void destroy();

}
</code></pre>
<p>通常，我们会实现 Filter 接口中的 doFilter 方法。关于过滤器的详细内容，你可以结合 08 讲“[管道过滤：如何基于 Spring Security 过滤器扩展安全性？]”做一下回顾。基于过滤器，我们可以将 ServletRequest 转化为一个 HttpServletRequest 对象，并从该对象中获取“Authorization”消息头，示例代码如下所示：</p>
<pre><code>@Component

public class AuthorizationHeaderFilter implements Filter {



    @Override

    public void doFilter(ServletRequest servletRequest, ServletResponse servletResponse, FilterChain filterChain)

            throws IOException, ServletException {

 

        HttpServletRequest httpServletRequest = (HttpServletRequest) servletRequest;

 

        AuthorizationHeaderHolder.getAuthorizationHeader().setAuthorizationHeader(httpServletRequest.getHeader(AuthorizationHeader.AUTHORIZATION_HEADER));



        filterChain.doFilter(httpServletRequest, servletResponse);

    }

 

    @Override

    public void init(FilterConfig filterConfig) throws ServletException {}

 

    @Override

    public void destroy() {}

}
</code></pre>
<p>请注意，这里我们<strong>把从 HTTP 请求中获取的“Authorization”消息头保存到了一个 AuthorizationHeaderHolder 对象中</strong>。从命名上看，AuthorizationHeader 对象代表的就是 HTTP 中“Authorization” 消息头，而 AuthorizationHeaderHolder 是该消息头对象的持有者。这种命名方式在 Spring 等主流开源框架中非常常见。</p>
<p>一般而言，以 -Holder 结尾的多是一种封装类，用于对原有对象添加线程安全等附加特性。这里的 AuthorizationHeaderHolder 就是这样一个封装类，如下所示：</p>
<pre><code>public class AuthorizationHeaderHolder {

    private static final ThreadLocal&lt;AuthorizationHeader&gt; authorizationHeaderContext = new ThreadLocal&lt;AuthorizationHeader&gt;();

 

    public static final AuthorizationHeader getAuthorizationHeader(){

        AuthorizationHeader header = authorizationHeaderContext.get();

 

        if (header == null) {

         header = new AuthorizationHeader();

            authorizationHeaderContext.set(header);

 

        }

        return authorizationHeaderContext.get();

    }

 

    public static final void setAuthorizationHeader(AuthorizationHeader header) {

        authorizationHeaderContext.set(header);

    }

}
</code></pre>
<p>可以看到，这里使用了 ThreadLocal 确保对 AuthorizationHeader 对象访问的线程安全性，AuthorizationHeader 定义如下，用于保存来自 HTTP 请求头的 JWT Token：</p>
<pre><code>@Component

public class AuthorizationHeader {

    public static final String AUTHORIZATION_HEADER = &quot;Authorization&quot;;



    private String authorizationHeader = new String();

 

    public String getAuthorizationHeader() {

        return authorizationHeader;

    }

 

    public void setAuthorizationHeader(String authorizationHeader) {

        this.authorizationHeader = authorizationHeader;

    }

}
</code></pre>
<p>现在，对于每一个 HTTP 请求，我们都能获取其中的 Token 并将其保存在上下文对象中。剩下的唯一问题就是如何通过 RestTemplate 将这个 Token 继续传递到下一个服务中，以便下一个服务也能从 HTTP 请求中获取 Token 并继续向后传递，从而确保 Token 在整个调用链中持续传播。要想实现这一目标，我们需要对 RestTemplate 进行一些设置，如下所示：</p>
<pre><code>@Bean

public RestTemplate getCustomRestTemplate() {

        RestTemplate template = new RestTemplate();

        List&lt;ClientHttpRequestInterceptor&gt; interceptors = template.getInterceptors();

        if (interceptors == null) {

           template.setInterceptors(Collections.singletonList(new AuthorizationHeaderInterceptor()));

        } else {

           interceptors.add(new AuthorizationHeaderInterceptor());

           template.setInterceptors(interceptors);

        }

 

        return template;

}
</code></pre>
<p>RestTemplate 允许开发人员添加自定义的拦截器 Interceptor，拦截器本质上与过滤器的功能类似，用于对传入的 HTTP 请求进行定制化处理。例如，上述代码中的 AuthorizationHeaderInterceptor 的作用就是在 HTTP 请求的消息头中嵌入保存在 AuthorizationHeaderHolder 中的 JWT Token，如下所示：</p>
<pre><code>public class AuthorizationHeaderInterceptor implements ClientHttpRequestInterceptor {

 

    @Override

    public ClientHttpResponse intercept(

            HttpRequest request, byte[] body, ClientHttpRequestExecution execution)

            throws IOException {

 

        HttpHeaders headers = request.getHeaders();

        headers.add(AuthorizationHeader.AUTHORIZATION_HEADER, AuthorizationHeaderHolder.getAuthorizationHeader().getAuthorizationHeader());

 

        return execution.execute(request, body);

    }

}
</code></pre>
<p>至此，在微服务中使用 JWT 的方法已经介绍完毕。关于 JWT 还有一部分内容我们没有介绍，即如何扩展 JWT 中所持有的数据结构，我们会在接下来的案例系统中结合具体的业务场景对这块内容进行补充。</p>
<h3>小结与预告</h3>
<p>这是介绍微服务安全性知识体系的最后一个课时，关注的是<strong>认证问题而不是授权问题</strong>，为此我们引入了 JWT 机制。JWT 本质上也是一种 Token，只不过提供了标准化的规范定义，可以与 OAuth2 协议进行集成。我们使用 JWT 时，也可以将各种信息添加到这种 Token 中，并在微服务访问链路中进行传播。</p>
<p>这里给你留一道思考题：如果想要确保 JWT 在各个微服务中进行有效传播，需要怎么做？</p>
<p>介绍完 JWT，下一讲又会介绍一个新的案例。我们将基于 Spring Security 和 Spring Cloud 构建一个 SpringOAuth2 案例系统，并给出微服务架构中实现服务安全访问的详细过程。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="14&#32;&#32;资源保护：如何基于&#32;OAuth2&#32;协议配置授权过程？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="16&#32;&#32;案例实战：基于&#32;Spring&#32;Security&#32;和&#32;Spring&#32;Cloud&#32;构建微服务安全架构.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script data-cfasync="false" src="../../cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script><script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434dd53d9870ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
</body>
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-NPSEEVD756"></script>
<script>
    window.dataLayer = window.dataLayer || [];

    function gtag() {
        dataLayer.push(arguments);
    }

    gtag('js', new Date());
    gtag('config', 'G-NPSEEVD756');
    var path = window.location.pathname
    var cookie = getCookie("lastPath");
    console.log(path)
    if (path.replace("/", "") === "") {
        if (cookie.replace("/", "") !== "") {
            console.log(cookie)
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/Spring%20Security%20%E8%AF%A6%E8%A7%A3%E4%B8%8E%E5%AE%9E%E6%93%8D/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
        }
    } else {
        setCookie("lastPath", path)
    }

    function setCookie(cname, cvalue) {
        var d = new Date();
        d.setTime(d.getTime() + (180 * 24 * 60 * 60 * 1000));
        var expires = "expires=" + d.toGMTString();
        document.cookie = cname + "=" + cvalue + "; " + expires + ";path = /";
    }

    function getCookie(cname) {
        var name = cname + "=";
        var ca = document.cookie.split(';');
        for (var i = 0; i < ca.length; i++) {
            var c = ca[i].trim();
            if (c.indexOf(name) === 0) return c.substring(name.length, c.length);
        }
        return "";
    }
</script>

</html>
