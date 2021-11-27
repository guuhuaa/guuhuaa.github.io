<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>13  授权体系：如何构建 OAuth2 授权服务器？.md</title>
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

                    <a class="current-tab" href="13&#32;&#32;授权体系：如何构建&#32;OAuth2&#32;授权服务器？.md">13  授权体系：如何构建 OAuth2 授权服务器？.md</a>
                    

                </li>
                <li>

                    
                    <a href="14&#32;&#32;资源保护：如何基于&#32;OAuth2&#32;协议配置授权过程？.md">14  资源保护：如何基于 OAuth2 协议配置授权过程？.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;&#32;令牌扩展：如何使用&#32;JWT&#32;实现定制化&#32;Token？.md">15  令牌扩展：如何使用 JWT 实现定制化 Token？.md</a>

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
                        <div><h1>13  授权体系：如何构建 OAuth2 授权服务器？</h1>
<p>上一讲我们讨论了 OAuth2 协议的详细内容，相信你已经了解了可以使用 OAuth2 协议实现微服务之间访问的授权。但是在此之前，我们需要在微服务系统中构建 OAuth2 授权服务器。今天我们就基于 Spring Security 框架，讨论如何构建这一授权服务器，并基于常用的密码模式生成对应的 Token，从而为下一讲中的服务访问控制提供基础。</p>
<h3>构建 OAuth2 授权服务器</h3>
<p>从表现形式上看，OAuth2 授权服务器也是一个独立的微服务，因此构建授权服务器的方法也是<strong>创建一个 Spring Boot 应用程序</strong>，我们需要引入对应的 Maven 依赖，如下所示：</p>
<pre><code>&lt;dependency&gt;

    &lt;groupId&gt;org.springframework.security.oauth&lt;/groupId&gt;

    &lt;artifactId&gt;spring-security-oauth2&lt;/artifactId&gt;

&lt;/dependency&gt;
</code></pre>
<p>这里的 spring-security-oauth2 就是来自 Spring Security 中的 OAuth2 库。现在 Maven 依赖已经添加完毕，下一步就是构建 Bootstrap 类作为访问的入口：</p>
<pre><code>@SpringBootApplication

@EnableAuthorizationServer

public class AuthorizationServer {

	

    public static void main(String[] args) {

        SpringApplication.run(AuthorizationServer.class, args);

    }

}
</code></pre>
<p>请注意，这里出现了一个新的注解 @EnableAuthorizationServer，这个注解的作用在于<strong>为微服务运行环境提供一个基于 OAuth2 协议的授权服务</strong>，该授权服务会暴露一系列基于 RESTful 风格的端点（例如 /oauth/authorize 和 /oauth/token）供 OAuth2 授权流程使用。</p>
<p>构建 OAuth2 授权服务只是集成 OAuth2 协议的第一步，授权服务器是一种<strong>集中式系统</strong>，管理着所有与安全性流程相关的客户端和用户信息。因此，接下来我们需要在授权服务器中对这些基础信息进行初始化，而 Spring Security 为我们提供了各种配置类来实现这一目标。</p>
<h3>设置客户端和用户认证信息</h3>
<p>上一讲我们提到 OAuth2 协议存在四种授权模式，并提到在微服务架构中，密码模式以其简单性得到了广泛的应用。在接下来的内容中，我们就以密码模式为例展开讲解。</p>
<p>在密码模式下，用户向客户端提供用户名和密码，并将用户名和密码发给授权服务器从而请求 Token。授权服务器首先会对密码凭证信息进行认证，确认无误后，向客户端发放 Token。整个流程如下图所示：</p>
<p><img src="assets/Cgp9HWDwB2GATe64AAEacKakyHk379.jpg" alt="Drawing 0.png" /></p>
<p>密码模式授权流程示意图</p>
<p>请注意，授权服务器在这里执行认证操作的目的是<strong>验证传入的用户名和密码是否正确</strong>。在密码模式下，这一步是必需的，如果采用其他授权模式，不一定会有用户认证这一环节。</p>
<p>确定采用密码模式后，我们来看为了实现这一授权模式，需要对授权服务器做哪些开发工作。首先我们需要设置一些基础数据，包括客户端信息和用户信息。</p>
<h4>设置客户端信息</h4>
<p>我们先来看如何设置客户端信息。设置客户端时，用到的配置类是 ClientDetailsServiceConfigurer，该配置类用来配置客户端详情服务 ClientDetailsService。用于描述客户端详情的 ClientDetails 接口则包含了与安全性控制相关的多个重要方法，该接口中的部分方法定义如下：</p>
<pre><code>public interface ClientDetails extends Serializable {

 

    	//客户端唯一性 Id

    	String getClientId();



    	//客户端安全码

    	String getClientSecret();



    	//客户端的访问范围

    	Set&lt;String&gt; getScope();



    	//客户端可以使用的授权模式

    	Set&lt;String&gt; getAuthorizedGrantTypes();

    	…

}
</code></pre>
<p>上述代码中的几个属性都与日常开发工作息息相关。</p>
<p>首先 ClientId 是一个必备属性，用来唯一标识客户的 Id，而 ClientSecret 代表客户端安全码。这里的 Scope 用来限制客户端的访问范围，如果这个属性为空，客户端就拥有全部的访问范围。常见的设置方式可以是 webclient 或 mobileclient，分别代表 Web 端和移动端。</p>
<p>最后，authorizedGrantTypes 代表客户端可以使用的授权模式，可选的范围包括代表授权码模式的 authorization_code、代表隐式授权模式 implicit、代表密码模式的 password 以及代表客户端凭据模式的 client_credentials。这个属性在设置上也<strong>可以添加 refresh_token，通过刷新操作获取以上授权模式下产生的新 Token</strong>。</p>
<p>和实现认证过程类似，Spring Security 也提供了 AuthorizationServerConfigurerAdapter 这个配置适配器类来简化配置类的使用方式。我们可以通过继承该类并覆写其中的 configure(ClientDetailsServiceConfigurer clients) 方法进行配置。使用 AuthorizationServerConfigurerAdapter 进行客户端信息配置的基本代码结构如下：</p>
<pre><code>@Configuration

public class SpringAuthorizationServerConfigurer extends AuthorizationServerConfigurerAdapter {

 

	@Override

	public void configure(ClientDetailsServiceConfigurer clients) throws Exception {

 

		clients.inMemory()

            .withClient(&quot;spring&quot;)

            .secret(&quot;{noop}spring_secret&quot;)

            .authorizedGrantTypes(&quot;refresh_token&quot;, &quot;password&quot;, &quot;client_credentials&quot;)

            .scopes(&quot;webclient&quot;, &quot;mobileclient&quot;);

	}

}
</code></pre>
<p>可以看到，我们创建了一个 SpringAuthorizationServerConfigure r类来继承 AuthorizationServerConfigurerAdapter，并通过 ClientDetailsServiceConfigurer 配置类设置了授权模式为密码模式。在授权服务器中存储客户端信息有两种方式，一种就是如上述代码所示的<strong>基于内存级别的存储</strong>，另一种则是<strong>通过 JDBC 在数据库中存储详情信息</strong>。为了简单起见，这里使用了内存级别的存储方式。</p>
<p>同时我们注意到，在设置客户端安全码时使用了&quot;{noop}spring_secret&quot;这种格式。这是因为在 Spring Security 5 中统一使用 PasswordEncoder 对密码进行编码，在设置密码时要求格式为“{id}password”。而这里的前缀“{noop}”就是代表具体 PasswordEncoder 的 id，表示我们使用的是 NoOpPasswordEncoder。关于 PasswordEncoder，你可以回顾[“密码安全：Spring Security 中包含哪些加解密技术？”]一讲中的内容。</p>
<p>我们已经在前面的内容中提到，@EnableAuthorizationServer 注解会暴露一系列的端点，而授权过程是使用 AuthorizationEndpoint 这个端点进行控制的。要想对该端点的行为进行配置，你可以使用 AuthorizationServerEndpointsConfigurer 这个配置类。和 ClientDetailsServiceConfigurer 配置类一样，我们也通过使用 AuthorizationServerConfigurerAdapter 配置适配器类进行配置。</p>
<p>因为我们指定了授权模式为密码模式，而密码模式包含认证环节。所以针对 AuthorizationServerEndpointsConfigurer 配置类需要指定一个认证管理器 AuthenticationManager，用于对用户名和密码进行认证。同样因为我们指定了基于密码的授权模式，所以需要指定一个自定义的 UserDetailsService 来替换全局的实现。关于 UserDetailsService 我们已经在[“用户认证：如何使用 Spring Security 构建用户认证体系？”]一讲中做了详细的讨论，我们明确可以通过如下代码来配置 AuthorizationServerEndpointsConfigurer：</p>
<pre><code>@Configuration

public class SpringAuthorizationServerConfigurer extends AuthorizationServerConfigurerAdapter {

 

	@Autowired

	private AuthenticationManager authenticationManager;

 

	@Autowired

	private UserDetailsService userDetailsService;

 

	@Override

	public void configure(AuthorizationServerEndpointsConfigurer endpoints) throws Exception {

		endpoints.authenticationManager(authenticationManager).userDetailsService(userDetailsService);

	} 

}
</code></pre>
<p>至此，客户端设置工作全部完成，我们所做的事情就是<strong>实现了一个自定义的 SpringAuthorizationServerConfigurer 配置类并覆写了对应的配置方法</strong>。</p>
<h4>设置用户认证信息</h4>
<p>设置用户认证信息所依赖的配置类是 WebSecurityConfigurer 类，Spring Security 同样提供了 WebSecurityConfigurerAdapter 类来简化该配置类的使用方式，我们可以继承 WebSecurityConfigurerAdapter 类并且覆写其中的 configure() 的方法来完成配置工作。</p>
<p>关于 WebSecurityConfigurer 配置类，我们首先需要明确配置的内容。实际上，设置用户信息非常简单，<strong>只需要指定用户名（User）、密码（Password）和角色（Role）这三项数据</strong>即可，如下所示：</p>
<pre><code>@Configuration

public class SpringWebSecurityConfigurer extends WebSecurityConfigurerAdapter {

 

	@Override

	@Bean

	public AuthenticationManager authenticationManagerBean() throws Exception {

		return super.authenticationManagerBean();

	}

 

	@Override

	@Bean

	public UserDetailsService userDetailsServiceBean() throws Exception {

		return super.userDetailsServiceBean();

	}

 

	@Override

	protected void configure(AuthenticationManagerBuilder builder) throws Exception {

		builder

            .inMemoryAuthentication()

            .withUser(&quot;spring_user&quot;)

            .password(&quot;{noop}password1&quot;)

            .roles(&quot;USER&quot;)

            .and()

			.withUser(&quot;spring_admin&quot;)

            .password(&quot;{noop}password2&quot;)

            .roles(&quot;USER&quot;, &quot;ADMIN&quot;);

	}

}
</code></pre>
<p>结合上面的代码，我们看到构建了具有不同角色和密码的两个用户，<strong>请注意&quot;spring_user&quot;代表的角色是一个普通用户，&quot;spring_admin&quot;则具有管理员角色</strong>。我们在设置密码时，同样需要添加前缀“{noop}”。同时，我们还看到 authenticationManagerBean()和 userDetailsServiceBean() 方法分别返回了父类的默认实现，而这里返回的 UserDetailsService 和 AuthenticationManager 在前面设置客户端时会用到。这里使用的用户认证机制你也可以回顾[“用户认证：如何使用 Spring Security 构建用户认证体系？”]中的内容。</p>
<h3>生成 Token</h3>
<p>现在，OAuth2 授权服务器已经构建完毕，启动这个授权服务器，我们就可以获取 Token。我们在构建 OAuth2 服务器时已经提到授权服务器中会暴露一批端点供 HTTP 请求进行访问，而获取 Token 的端点就是<a href="http://localhost:8080/oauth/token">http://localhost:8080/oauth/token</a>。在使用该端点时，我们需要提供前面配置的客户端信息和用户信息。</p>
<p>这里使用 Postman 来模拟 HTTP 请求，客户端信息设置方式如下图所示：</p>
<p><img src="assets/Cgp9HWDwB76Ad4WHAAFWqbAkk6I359.jpg" alt="Drawing 1.png" /></p>
<p>客户端信息设置示意图</p>
<p>我们在“Authorization”请求头中指定认证类型为“Basic Auth”，然后设置客户端名称和客户端安全码分别为“spring”和“spring_secret”。</p>
<p>接下来我们指定针对授权模式的专用配置信息。首先是用于指定授权模式的 grant_type 属性，以及用于指定客户端访问范围的 scope 属性，这里分别设置为 “password”和“webclient”。既然设置了密码模式，所以也需要指定用户名和密码用于识别用户身份，这里，我们以“spring_user”这个用户为例进行设置，如下图所示：</p>
<p><img src="assets/Cgp9HWDwB_CAVjFCAAEqxkNRiNY244.jpg" alt="Drawing 2.png" /></p>
<p>用户信息设置示意图</p>
<p>在 Postman 中执行这个请求，会得到如下所示的返回结果：</p>
<pre><code>{

    &quot;access_token&quot;: &quot;0efa61be-32ab-4351-9dga-8ab668ababae&quot;,

    &quot;token_type&quot;: &quot;bearer&quot;,

    &quot;refresh_token&quot;: &quot;738c42f6-79a6-457d-8d5a-f9eab0c7cc5e&quot;,

    &quot;expires_in&quot;: 43199,

    &quot;scope&quot;: &quot;webclient&quot;

}
</code></pre>
<p>可以看到，除了作为请求参数的 scope，这个返回结果中还包含了 access_token、token_type、refresh_token 和 expires_in 等属性。这些属性都很重要，我们在上一讲中都做了详细的介绍。当然，因为每次请求生成的 Token 都是唯一的，所以你在尝试时获取的结果可能与我的不同。</p>
<h3>小结与预告</h3>
<p>对微服务访问进行安全性控制的首要条件是<strong>生成一个访问 Token</strong>。这一讲我们从构建 OAuth2 服务器讲起，基于密码模式给出了如何设置客户端信息、用户认证信息以及最终生成 Token 的实现过程。这个过程中需要开发人员熟悉 OAuth2 协议的相关概念以及 Spring Security 框架中提供的各项配置功能。</p>
<p>本讲内容总结如下：</p>
<p><img src="assets/CioPOWDwCAOAI2-LAAGPXTcuzx0579.jpg" alt="13-2.jpg" /></p>
<p>最后给你留一道思考题：基于密码模式，你能说明生成 Token 需要哪些具体的开发步骤吗？</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="12&#32;&#32;开放协议：OAuth2&#32;协议解决的是什么问题？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="14&#32;&#32;资源保护：如何基于&#32;OAuth2&#32;协议配置授权过程？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434dbf0fbf70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
