<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>11  案例实战：使用 Spring Security 高级主题保护 Web 应用.md</title>
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

                    <a class="current-tab" href="11&#32;&#32;案例实战：使用&#32;Spring&#32;Security&#32;高级主题保护&#32;Web&#32;应用.md">11  案例实战：使用 Spring Security 高级主题保护 Web 应用.md</a>
                    

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
                        <div><h1>11  案例实战：使用 Spring Security 高级主题保护 Web 应用</h1>
<p>前面几讲我们系统介绍了 Spring Security 提供的一些高级功能，包括过滤器、CSRF 保护、CORS 以及全局方法，这些都是非常实用的功能特性。作为阶段性的总结，今天的内容将利用这些功能特性构建在安全领域中的一种典型的认证机制，即<strong>多因素认证</strong>（Multi-Factor Authentication，MFA）机制。</p>
<h3>案例设计和初始化</h3>
<p>在今天的案例中，我们构建多因素认证的思路并不是采用第三方成熟的解决方案，而是基于 Spring Security 的功能特性来自己设计并实现一个简单而完整的认证机制。</p>
<h4>多因素认证设计</h4>
<p>多因素认证是一种安全访问控制的方法，基本的设计理念在于<strong>用户想要访问最终的资源，至少需要通过两种以上的认证机制</strong>。</p>
<p>那么，我们如何实现多种认证机制呢？一种常见的做法是分成两个步骤，第一步通过用户名和密码获取一个认证码（Authentication Code），第二步基于用户名和这个认证码进行安全访问。基于这种多因素认证的基本执行流程如下图所示：</p>
<p><img src="assets/Cgp9HWDcHxyASKleAAC5AmJ3Hwc285.png" alt="Drawing 0.png" /></p>
<p>多因素认证的实现方式示意图</p>
<h4>系统初始化</h4>
<p>为了实现多因素认证，我们需要构建一个独立的认证服务 Auth-Service，该服务<strong>同时提供了基于用户名+密码以及用户名+认证码的认证形式</strong>。当然，实现认证的前提是构建用户体系，因此我们需要提供如下所示的 User 实体类：</p>
<pre><code>@Entity

public class User {

 

    @Id

    @GeneratedValue(strategy = GenerationType.IDENTITY)

    private Integer id;

    

    private String username;

    private String password;

}
</code></pre>
<p>可以看到，User 对象中包含了用户名 Username 和密码 Password 的定义。同样的，在如下所示的代表认证码的 AuthCode 对象中包含了用户名 Username 和具体的认证码 Code 字段的定义：</p>
<pre><code>@Entity

public class AuthCode {

 

    @Id

    @GeneratedValue(strategy = GenerationType.IDENTITY)

    private Integer id;

    

    private String username;

    private String code;   

}
</code></pre>
<p>基于 User 和 AuthCode 实体对象，我们也给出创建数据库表的对应 SQL 定义，如下所示：</p>
<pre><code>CREATE TABLE IF NOT EXISTS `spring_security_demo`.`user` (

    `id` INT NOT NULL AUTO_INCREMENT,

    `username` VARCHAR(45) NULL,

    `password` TEXT NULL,

    PRIMARY KEY (`id`));

 

CREATE TABLE IF NOT EXISTS `spring_security_demo`.`auth_code` (

    `id` INT NOT NULL AUTO_INCREMENT,

    `username` VARCHAR(45) NOT NULL,

    `code` VARCHAR(45) NULL,

    PRIMARY KEY (`id`));
</code></pre>
<p>有了认证服务，接下来我们需要构建一个业务服务 Business-Service，该业务服务通过集成认证服务，完成具体的认证操作，并返回访问令牌（Token）给到客户端系统。因此，从依赖关系上讲，Business-Service 会调用 Auth-Service，如下图所示：</p>
<p><img src="assets/Cgp9HWDcHyuAT3auAACddvz56Cc067.png" alt="Drawing 2.png" /></p>
<p>Business-Service 调用 Auth-Service 关系图</p>
<p>接下来，我们分别从这两个服务入手，实现多因素认证机制。</p>
<h3>实现多因素认证机制</h3>
<p>对于多因素认证机制而言，<strong>实现认证服务是基础</strong>，但难度并不大，我们往下看。</p>
<h4>实现认证服务</h4>
<p>从表现形式上看，认证服务也是一个 Web 服务，所以内部需要<strong>通过构建 Controller 层组件实现 HTTP 端点的暴露</strong>。为此，我们构建了如下所示的 AuthController：</p>
<pre><code>@RestController

public class AuthController {

 

    @Autowired

    private UserService userService;

 

    //添加User

    @PostMapping(&quot;/user/add&quot;)

    public void addUser(@RequestBody User user) {

        userService.addUser(user);

    }

 

    //通过用户名+密码对用户进行首次认证

    @PostMapping(&quot;/user/auth&quot;)

    public void auth(@RequestBody User user) {

        userService.auth(user);

    }

 

    //通过用户名+认证码进行二次认证

    @PostMapping(&quot;/authcode/check&quot;)

    public void check(@RequestBody AuthCode authCode, HttpServletResponse response) {

        if (userService.check(authCode)) {

            response.setStatus(HttpServletResponse.SC_OK);

        } else {

            response.setStatus(HttpServletResponse.SC_FORBIDDEN);

        }

    }

}
</code></pre>
<p>可以看到，这里除了一个添加用户信息的 HTTP 端点之外，我们分别实现了通过用户名+密码对用户进行首次认证的&quot;/user/auth&quot;端点，以及通过用户名+认证码进行二次认证的&quot;/authcode/check&quot;端点。</p>
<p>这两个核心端点背后的实现逻辑都位于 UserService 中，我们先来看其中的 auth() 方法：</p>
<pre><code>public void auth(User user) {

        Optional&lt;User&gt; o =

                userRepository.findUserByUsername(user.getUsername());

 

        if(o.isPresent()) {

            User u = o.get();

            if (passwordEncoder.matches(user.getPassword(), u.getPassword())) {

                 //生成或刷新认证码

                generateOrRenewAutoCode(u);

            } else {

                throw new BadCredentialsException(&quot;Bad credentials.&quot;);

            }

        } else {

            throw new BadCredentialsException(&quot;Bad credentials.&quot;);

        }

}
</code></pre>
<p>上述代码中的关键流程就是在<strong>完成用户密码匹配之后的刷新认证码流程</strong>，负责实现该流程的 generateOrRenewAutoCode() 方法如下所示：</p>
<pre><code>private void generateOrRenewAutoCode (User u) {

        String generatedCode = GenerateCodeUtil.generateCode();

 

        Optional&lt;AuthCode&gt; autoCode = autoCodeRepository.findAuthCodeByUsername(u.getUsername());

        if (autoCode.isPresent()) {//如果存在认证码，则刷新该认证码

            AuthCode code = autoCode.get();

            code.setCode(generatedCode);

        } else {//如果没有找到认证码，则生成并保存一个新的认证码

            AuthCode code = new AuthCode();

            code.setUsername(u.getUsername());

            code.setCode(generatedCode);

            autoCodeRepository.save(code);

        }

}
</code></pre>
<p>上述方法的流程也很明确，首先通过调用工具类 GenerateCodeUtil 的 generateCode() 方法生成一个认证码，然后根据当前数据库中的状态决定是否对已有的认证码进行刷新，或者直接生成一个新的认证码并保存。因此，<strong>每次调用 UserService 的 auth() 方法就相当于对用户的认证码进行了动态重置</strong>。</p>
<p>一旦用户获取了认证码，并通过该认证码访问系统，认证服务就可以对该认证码进行校验，从而确定其是否有效。对认证码进行验证的方法如下所示：</p>
<pre><code>public boolean check(AuthCode authCodeToValidate) {

        Optional&lt;AuthCode&gt; authCode = autoCodeRepository.findAuthCodeByUsername(authCodeToValidate.getUsername());

        if (authCode.isPresent()) {

            AuthCode authCodeInStore = authCode.get();

            if (authCodeToValidate.getCode().equals(authCodeInStore.getCode())) {

                return true;

            }

        }

 

        return false;

}
</code></pre>
<p>这里的逻辑也很简单，就是<strong>把从数据库中获取的认证码与用户传入的认证码进行比对</strong>。</p>
<p>至此，认证服务的核心功能已经构建完毕，下面我们来看业务服务的实现过程。</p>
<h4>实现业务服务</h4>
<p>在业务服务中，势必需要<strong>调用认证服务提供的 HTTP 端点</strong>来完成用户认证和认证码认证这两个核心的认证操作。因此，我们需要构建一个认证服务的客户端组件完成远程调用。在案例中，我们参考设计模式中的门面（Facade）模式的设计理念，将这个组件命名为 AuthenticationServerFacade，也就是说它是认证服务的一种门面组件，定义如下：</p>
<pre><code>@Component

public class AuthenticationServerFacade {

 

    @Autowired

    private RestTemplate rest;

 

    @Value(&quot;${auth.server.base.url}&quot;)

    private String baseUrl;

 

    public void checkPassword(String username, String password) {

        String url = baseUrl + &quot;/user/auth&quot;;

 

        User body = new User();

        body.setUsername(username);

        body.setPassword(password);

 

        HttpEntity&lt;User&gt; request = new HttpEntity&lt;User&gt;(body);

 

        rest.postForEntity(url, request, Void.class);

    }

 

    public boolean checkAuthCode(String username, String code) {

        String url = baseUrl + &quot;/authcode/check&quot;;

 

        User body = new User();

        body.setUsername(username);

        body.setCode(code);

 

        HttpEntity&lt;User&gt; request = new HttpEntity&lt;User&gt;(body);

        

        ResponseEntity&lt;Void&gt; response = rest.postForEntity(url, request, Void.class);

 

        return response.getStatusCode().equals(HttpStatus.OK);

    }

}
</code></pre>
<p>这里的 baseUrl 就是认证服务暴露的服务地址，我们使用 RestTemplate 模板类发起对认证服务的远程调用，并根据返回值来判断认证是否通过。</p>
<p>有了 AuthenticationServerFacade，我们就可以在业务服务中集成认证服务了。我们在每次请求的处理过程中完成这种集成工作，此时需要用到拦截器，而这种集成工作显然需要依赖于认证管理器 AuthenticationManager。因此，我们可以先来设计并实现如下所示的 CustomAuthenticationFilter 代码结构：</p>
<pre><code>@Component

public class CustomAuthenticationFilter extends OncePerRequestFilter {

 

    @Autowired

    private AuthenticationManager manager;

 

    @Override

    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain) throws ServletException, IOException {

        String username = request.getHeader(&quot;username&quot;);

        String password = request.getHeader(&quot;password&quot;);

        String code = request.getHeader(&quot;code&quot;);

 

        //使用 AuthenticationManager 处理认证过程

    }

}
</code></pre>
<p>上述代码中第一个需要关注的点是 CustomAuthenticationFilter 所扩展的基类 OncePerRequestFilter。顾名思义，OncePerRequestFilter 能够确保在一次请求中只执行一次过滤器逻辑，不会发生多次重复执行的情况。这里我们分别从 HTTP 请求头中获取了用户名 username、密码 password 以及认证码 code 这三个参数，并尝试使用 AuthenticationManager 完成认证。基于[03 讲“认证体系：如何深入理解 Spring Security 的用户认证机制？”]中的讨论，我们知道 AuthenticationManager 的背后实际上使用了 AuthenticationProvider 执行具体的认证操作。</p>
<p>再来回想一下认证服务中提供的两种认证操作，一种是基于用户名和密码完成用户认证，一种是基于用户名和认证码完成针对认证码的认证。因此，我们需要针对这两种操作分别实现不同的 AuthenticationProvider。例如，如下所示的 UsernamePasswordAuthenticationProvider 就实现了针对用户名和密码的认证操作：</p>
<pre><code>@Component

public class UsernamePasswordAuthenticationProvider implements AuthenticationProvider {

 

    @Autowired

    private AuthenticationServerFacade authServer;

 

    public Authentication authenticate(Authentication authentication) throws AuthenticationException {

        String username = authentication.getName();

        String password = String.valueOf(authentication.getCredentials());

        

        //调用认证服务完成认证

        authServer.checkPassword(username, password);

 

        return new UsernamePasswordAuthenticationToken(username, password);

    }

 

    public boolean supports(Class&lt;?&gt; aClass) {

        return UsernamePasswordAuthentication.class.isAssignableFrom(aClass);

    }

}
</code></pre>
<p>可以看到，这里使用了 AuthenticationServerFacade 门面类来完成对认证服务的远程调用。类似地 ，我们也可以构建针对认证码的 AuthenticationProvider，即如下所示的 AuthCodeAuthenticationProvider：</p>
<pre><code>@Component

public class AuthCodeAuthenticationProvider implements AuthenticationProvider {

 

    @Autowired

    private AuthenticationServerFacade authServer;

 

    public Authentication authenticate(Authentication authentication) throws AuthenticationException {

        String username = authentication.getName();

        String code = String.valueOf(authentication.getCredentials());

        

        //调用认证服务完成认证

        boolean result = authServer.checkAuthCode(username, code);

 

        if (result) {

            return new AuthCodeAuthentication(username, code);

        } else {

            throw new BadCredentialsException(&quot;Bad credentials.&quot;);

        }

    }

 

    public boolean supports(Class&lt;?&gt; aClass) {

        return AuthCodeAuthentication.class.isAssignableFrom(aClass);

    }

}
</code></pre>
<p>请注意，无论是 UsernamePasswordAuthenticationProvider 还是 AuthCodeAuthenticationProvider，所返回的 UsernamePasswordAuthentication 和 AuthCodeAuthentication 都是<strong>自定义的认证信息类</strong>，它们都继承了 Spring Security 自带的 UsernamePasswordAuthenticationToken。</p>
<p>现在，让我们回到过滤器组件 CustomAuthenticationFilter，并提供对它的完整实现，如下所示：</p>
<pre><code>@Component

public class CustomAuthenticationFilter extends OncePerRequestFilter {

 

    @Autowired

    private AuthenticationManager manager;

 

    @Override

    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain) throws ServletException, IOException {

        String username = request.getHeader(&quot;username&quot;);

        String password = request.getHeader(&quot;password&quot;);

        String code = request.getHeader(&quot;code&quot;);

 

        //如果认证码为空，说明需要先执行用户名/密码认证

        if (code == null) {

            Authentication a = new UsernamePasswordAuthentication(username, password);

            manager.authenticate(a);

        } else {

	        //如果认证码不为空，则执行认证码认证

            Authentication a = new AuthCodeAuthentication(username, code);

            manager.authenticate(a);

 

            //如果认证码认证通过，则通过 UUID 生成一个 Token 并添加在响应的消息头中

            String token = UUID.randomUUID().toString();

            response.setHeader(&quot;Authorization&quot;, token);

        }

 

    }

 

    @Override

    protected boolean shouldNotFilter(HttpServletRequest request) {

        return !request.getServletPath().equals(&quot;/login&quot;);

    }

}
</code></pre>
<p>CustomAuthenticationFilter 的实现过程比较简单，代码也都是自解释的，唯一需要注意的是<strong>在基于认证码的认证过程通过之后，我们会在响应中添加一个“Authorization”消息头，并使用 UUID 值作为 Token 进行返回</strong>。</p>
<p>针对上述代码，我们可以通过如下所示的类图进行总结：</p>
<p><img src="assets/CioPOWDcH0SAWPjtAAB7UfIfAyk803.png" alt="Drawing 4.png" /></p>
<p>多因素认证执行核心类图</p>
<p>最后，我们需要通过 Spring Security 中的配置体系确保各个类之间的有效协作。为此，我们构建了如下所示的 SecurityConfig 类：</p>
<pre><code>@Configuration

public class SecurityConfig extends WebSecurityConfigurerAdapter {

 

    @Autowired

    private CustomAuthenticationFilter customAuthenticationFilter;

 

    @Autowired

    private AuthCodeAuthenticationProvider authCodeAuthenticationProvider;

 

    @Autowired

    private UsernamePasswordAuthenticationProvider usernamePasswordAuthenticationProvider;

 

    @Override

    protected void configure(AuthenticationManagerBuilder auth) {

        auth.authenticationProvider(authCodeAuthenticationProvider)

            .authenticationProvider(usernamePasswordAuthenticationProvider);

    }

 

    @Override

    protected void configure(HttpSecurity http) throws Exception {

        http.csrf().disable();

 

        http.addFilterAt(

                customAuthenticationFilter,

                BasicAuthenticationFilter.class);

 

        http.authorizeRequests()

                .anyRequest().authenticated();

    }

 

    @Override

    @Bean

    protected AuthenticationManager authenticationManager() throws Exception {

        return super.authenticationManager();

    }

}
</code></pre>
<p>上述配置内容中，我们看到可以通过 addFilterAt() 方法添加自定义过滤器。关于过滤器使用方式的更多内容，你也可以参考[08 讲“管道过滤：如何基于 Spring Security 过滤器扩展安全性？”]的内容进行回顾。</p>
<p>关于案例的完整代码你可以在这里进行下载：<a href="https://github.com/lagouEdAnna/SpringSecurity-jianxiang/tree/main/MultiFactorAuthenticationDemo">https://github.com/lagouEdAnna/SpringSecurity-jianxiang/tree/main/MultiFactorAuthenticationDemo</a>。</p>
<h3>案例演示</h3>
<p>现在，让我们分别在本地启动认证服务和业务服务，请注意：认证服务的启动端口是 8080，而业务服务的启动端口是 9090。然后我们打开模拟 HTTP 请求的 Postman 并输入相关参数，如下所示：</p>
<p><img src="assets/CioPOWDcH1CAWsVIAACxvLoOLdE765.png" alt="Drawing 5.png" /></p>
<p>多因素认证的第一步认证示意图：基于用户名+密码</p>
<p>显然，该请求只传入了用户名和密码，所以会基于 UsernamePasswordAuthenticationProvider 执行认证过程，从而为用户“jianxiang”生成认证码。<strong>认证码是动态生成的，所以每次请求对应的结果都是不一样的</strong>，我通过查询数据库，获取该认证码为“9750”，你也可以自己做一些尝试。</p>
<p>有了认证码，相当于完成了多因素认证机制的第一步。接下来，我们再次基于这个认证码构建请求并获取响应结果，如下所示：</p>
<p><img src="assets/Cgp9HWDcH1mACUXeAADWBUPX0po513.png" alt="Drawing 7.png" /></p>
<p>多因素认证的第二步认证示意图：基于用户名+认证码</p>
<p>可以看到，通过传入正确的认证码，我们基于 AuthCodeAuthenticationProvider 完成了多因素认证机制中的第二步认证，并最终在 HTTP 响应中生成了一个“Authorization”消息头。</p>
<h3>小结与预告</h3>
<p>这一讲我们基于多因素认证机制展示了如何利用 Spring Security 中的一些高级主题保护 Web 应用程序的实现方法。多因素认证机制的实现需要构建多个自定义的 AuthenticationProvider，并通过拦截器完成对请求的统一处理。相信案例中展示的这些开发技巧会给你的日常开发工作带来帮助。</p>
<p>本讲内容总结如下：</p>
<p><img src="assets/Cgp9HWDcH2KAfoU3AAHK941R6Dk155.png" alt="Drawing 9.png" /></p>
<p>这里给你留一道思考题：在 Spring Security 中，如何利用过滤器实现对用户请求的定制化认证？</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="10&#32;&#32;全局方法：如何确保方法级别的安全访问？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="12&#32;&#32;开放协议：OAuth2&#32;协议解决的是什么问题？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434db62a4d70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
