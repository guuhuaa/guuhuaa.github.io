<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>14  资源保护：如何基于 OAuth2 协议配置授权过程？.md</title>
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

                    <a class="current-tab" href="14&#32;&#32;资源保护：如何基于&#32;OAuth2&#32;协议配置授权过程？.md">14  资源保护：如何基于 OAuth2 协议配置授权过程？.md</a>
                    

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
                        <div><h1>14  资源保护：如何基于 OAuth2 协议配置授权过程？</h1>
<p>上一讲我们学习了如何构建 OAuth2 授权服务器，并掌握了生成 Token 的系统方法。今天我们关注的重点是如何使用 Token 实现对服务访问的具体授权。在日常开发过程中，我们需要对每个服务的不同功能进行不同粒度的权限控制，并且希望这种控制方法足够灵活，能够确保不同服务根据业务场景动态调整权限控制体系。同时，在微服务架构中，我们还需要考虑如何在多个服务中对 Token 进行有效的传播，确保整个服务访问的链路都得到授权管理。借助 Spring Security 框架，实现这些需求都很简单，下面我们就来展开学习。</p>
<h3>在微服务中集成 OAuth2 授权机制</h3>
<p>我们知道在 OAuth2 协议中，单个微服务的定位就是资源服务器。Spring Security 框架为此提供了专门的 @EnableResourceServer 注解。通过<strong>在 Bootstrap 类中添加 @EnableResourceServer 注解</strong>，相当于声明该服务中的所有内容都是受保护的资源，示例代码如下所示：</p>
<pre><code>@SpringBootApplication

@EnableResourceServer

public class UserApplication {

 

    public static void main(String[] args) {

        SpringApplication.run(UserApplication.class, args);

    }

}
</code></pre>
<p>一旦我们在微服务中添加了 @EnableResourceServer 注解，该服务就会对所有的 HTTP 请求进行验证以确定 Header 部分中是否包含 Token 信息。如果没有 Token 信息，就会直接限制访问；如果有 Token 信息，则通过访问 OAuth2 服务器进行 Token 的验证。那么问题来了，每个微服务是如何与 OAuth2 服务器进行通信并获取传入 Token 的验证结果的呢？</p>
<p>要想回答这个问题，我们需要明确将 Token 传递给 OAuth2 授权服务器的目的是<strong>获取该 Token 中包含的用户和授权信息</strong>。这样，我们势必需要在各个微服务和 OAuth2 授权服务器之间建立起一种交互关系。我们可以在配置文件中添加如下所示的 security.oauth2.resource.userInfoUri 配置项来实现这一目标：</p>
<pre><code>security:

  oauth2:

    resource:

	  userInfoUri: http://localhost:8080/userinfo
</code></pre>
<p>这里的 <a href="http://localhost:8080/userinfo">http://localhost:8080/userinfo</a>指向 OAuth2 授权服务器中的一个自定义端点，实现方式如下所示：</p>
<pre><code>@RequestMapping(value = &quot;/userinfo&quot;, produces = &quot;application/json&quot;)

public Map&lt;String, Object&gt; user(OAuth2Authentication user) {

        Map&lt;String, Object&gt; userInfo = new HashMap&lt;&gt;();

        userInfo.put(&quot;user&quot;, user.getUserAuthentication().getPrincipal());

        userInfo.put(&quot;authorities&quot;, AuthorityUtils.authorityListToSet(

user.getUserAuthentication().getAuthorities()));

        return userInfo;

}
</code></pre>
<p>这个端点的作用就是获取可访问的那些受保护服务的用户信息。这里我们用到了 OAuth2Authentication 类，该类保存着用户的身份（Principal）和权限（Authority）信息。</p>
<p>当使用 Postman 访问 http://localhost:8080/userinfo 端点时，我们就需要传入一个有效的 Token。这里我们以上一讲中生成的 Token“0efa61be-32ab-4351-9dga-8ab668ababae”为例，在 HTTP 请求中添加一个“Authorization”请求头。请注意，因为我们使用的是 bearer 类型的 Token，所以需要<strong>在 access_token 的具体值之前加上“bearer”前缀</strong>。当然，我们也可以直接在“Authorization”页中选择协议类型为 OAuth 2.0，然后输入 Access Token，这样就相当于添加了请求头信息，如下图所示：</p>
<p><img src="assets/CioPOWDwBsmAdTfxAAF0kH4jkg4969.jpg" alt="图片.png" /></p>
<p>通过 Token 发起 HTTP 请求示意图</p>
<p>在后续的 HTTP 请求中，我们都将以这种方式发起对微服务的调用。该请求的结果如下所示：</p>
<pre><code>{

     &quot;user&quot;:{

         &quot;password&quot;:null,

         &quot;username&quot;:&quot;spring_user&quot;,

         &quot;authorities&quot;:[

             {

                 &quot;autority&quot;:&quot;ROLE_USER&quot;

             }

         ],

         &quot;accountNonExpired&quot;:true,

         &quot;accountNonLocker&quot;:true,

         &quot;credentialsNonExpired&quot;:true,

         &quot;enabled&quot;:true

     },

     &quot;authorities&quot;:[

         &quot;ROLE_USER&quot;

     ]

 }
</code></pre>
<p>我们知道“0efa61be-32ab-4351-9dga-8ab668ababae”这个 Token 是由“spring_user”这个用户生成的，可以看到该结果中包含了用户的用户名、密码以及该用户名所拥有的角色，这些信息与我们在上一讲中初始化的“spring_user”用户信息保持一致。我们也可以尝试使用“spring_admin”这个用户来重复上述过程。</p>
<h3>在微服务中嵌入访问授权控制</h3>
<p>在一个微服务系统中，每个微服务作为独立的资源服务器，对自身资源的保护粒度并不是固定的，可以根据需求对访问权限进行精细化控制。在 Spring Security 中，对访问的不同控制层级进行了抽象，形成了<strong>用户、角色和请求方法</strong>这三种粒度，如下图所示：</p>
<p><img src="assets/CioPOWDwBtmAMiWZAAFQfgXxt_0021.jpg" alt="image-2.png" /></p>
<p>用户、角色和请求方法三种控制粒度示意图</p>
<p>基于上图，我们可以对这三种粒度进行排列组合，形成用户、用户+角色以及用户+角色+请求方法这三种层级，这三种层级能够访问的资源范围逐一递减。用户层级是指只要是认证用户就能访问服务内的各种资源；而用户+角色层级在用户层级的基础上，还要求用户属于某一个或多个特定角色；最后的用户+角色+请求方法层级要求最高，能够对某些 HTTP 操作进行访问限制。接下来我们针对这三个层级展开讨论。</p>
<h4>用户层级的权限访问控制</h4>
<p>通过上一讲的学习，我们已经熟悉了通过扩展各种 ConfigurerAdapter 配置适配器类来实现自定义配置信息的方法。对于资源服务器而言，也存在一个 ResourceServerConfigurerAdapter 类，而我们的做法同样是<strong>继承该类并覆写它的 configure 方法</strong>，如下所示：</p>
<pre><code>@Configuration

public class ResourceServerConfiguration extends ResourceServerConfigurerAdapter {

 

    @Override

    public void configure(HttpSecurity httpSecurity) throws Exception{

        httpSecurity.authorizeRequests()

             .anyRequest()

             .authenticated();

    }

}
</code></pre>
<p>我们注意到，这个方法的入参是一个 HttpSecurity 对象，而上述配置中的 anyRequest().authenticated() 方法指定了访问该服务的任何请求都需要进行验证。因此，当我们使用普通的 HTTP 请求来访问 user-service 中的任何 URL 时，将会得到一个“unauthorized”的 401 错误信息。解决办法就是<strong>在 HTTP 请求中设置“Authorization”请求头并传入一个有效的 Token 信息</strong>，你可以模仿前面的示例做一些练习。</p>
<h4>用户+角色层级的权限访问控制</h4>
<p>对于某些安全性要求比较高的资源，我们不应该开放资源访问入口给所有的认证用户，而是需要<strong>限定访问资源的角色</strong>。针对不同的业务场景，我们可以判断哪些服务涉及核心业务流程，这些服务的 HTTP 端口不应该开放给普通用户，而是限定只有角色为“ADMIN”的管理员才能访问该服务。要想达到这种效果，实现方式也比较简单，就是在HttpSecurity 中通过 antMatchers() 和 hasRole() 方法指定想要限制的资源和角色。我们可以创建一个新 ResourceServerConfiguration 类实例并覆写它的 configure 方法，如下所示：</p>
<pre><code>@Configuration

public class ResourceServerConfiguration extends 

	ResourceServerConfigurerAdapter{

 

    @Override

	public void configure(HttpSecurity httpSecurity) throws Exception {

	 

        httpSecurity.authorizeRequests()

                .antMatchers(&quot;/order/**&quot;)

                .hasRole(&quot;ADMIN&quot;)

                .anyRequest()

                .authenticated();

    }

}
</code></pre>
<p>可以看到，这里使用了 05 讲[“访问授权：如何对请求的安全访问过程进行有效配置？”]中介绍的 Ant 匹配器实现了授权管理。现在，如果我们使用角色为“User”的 Token 访问这个服务，就会得到一个“access_denied”的错误信息。然后，我们使用上一讲中初始化的一个具有“ADMIN”角色的用户“spring_admin”来创建新的 Token，并再次访问该服务，就能得到正常的返回结果。</p>
<h4>用户+角色+操作层级的权限访问控制</h4>
<p>更进一步，我们还可以针对某个端点的某个具体 HTTP 方法进行控制。例如，如果我们认为对某个微服务中的“user”端点下的资源进行更新的风险很高，那么就可以在 HttpSecurity 的 antMatchers() 中添加 HttpMethod.PUT 限定。</p>
<pre><code>@Configuration

public class ResourceServerConfiguration extends ResourceServerConfigurerAdapter {

 

    @Override

    public void configure(HttpSecurity httpSecurity) throws Exception{

        httpSecurity.authorizeRequests()

                .antMatchers(HttpMethod.PUT, &quot;/user/**&quot;)

                .hasRole(&quot;ADMIN&quot;)

                .anyRequest()

                .authenticated();

    }

}
</code></pre>
<p>现在，我们使用普通“USER”角色生成的 Token，并调用&quot;/order/&quot;端点中的 Update 操作，同样会得到“access_denied”的错误信息。而尝试使用“ADMIN”角色生成的 Token 进行访问，就可以得到正常响应。</p>
<h3>在微服务中传播 Token</h3>
<p>我们知道一个微服务系统势必涉及多个服务之间的调用，并形成一个链路。因为访问所有服务的过程都需要进行访问权限的控制，所以我们需要确保生成的 Token 能够在服务调用链路中进行传播，如下图所示：</p>
<p><img src="assets/Cgp9HWDwBumAe_JvAAEWjcq9xMI017.jpg" alt="image-3.png" /></p>
<p>微服务中 Token 传播示意图</p>
<p>那么，如何实现上图中的 Token 传播效果呢？Spring Security 基于 RestTemplate 进行了封装，专门提供了一个用在 HTTP 请求中传播 Token 的 OAuth2RestTemplate 工具类。想要在业务代码中构建一个 OAuth2RestTemplate 对象，可以使用如下所示的示例代码：</p>
<pre><code>@Bean

public OAuth2RestTemplate oauth2RestTemplate(

	OAuth2ClientContext oauth2ClientContext,

    OAuth2ProtectedResourceDetails details) {

 

        return new OAuth2RestTemplate(details, oauth2ClientContext);

}
</code></pre>
<p>可以看到，通过传入 OAuth2ClientContext 和 OAuth2ProtectedResourceDetails，我们就可以创建一个 OAuth2RestTemplate 类。OAuth2RestTemplate 会把从 HTTP 请求头中获取的 Token 保存到一个 OAuth2ClientContext 上下文对象中，而OAuth2ClientContext 会把每个用户的请求信息控制在会话范围内，以确保不同用户的状态分离。另一方面，OAuth2RestTemplate 还依赖于 OAuth2ProtectedResourceDetails 类，该类封装了我们在上一讲中介绍过的clientId、客户端安全码 clientSecret、访问范围 scope 等属性。</p>
<p>一旦 OAuth2RestTemplate 创建成功，我们就可以使用它对某一个远程服务进行访问，实现代码如下所示：</p>
<pre><code>@Component

public class OrderServiceClient {

 

    @Autowired

	OAuth2RestTemplate restTemplate;

 

    public Order getOrderById(String orderId){



        ResponseEntity&lt;Order&gt; result =

                restTemplate.exchange(

                        &quot;http://orderservice/order/{orderId}&quot;,

                        HttpMethod.GET,

                        null, Order.class, orderId);



        Order order = result.getBody();



        return order;

    }

}
</code></pre>
<p>显然，基于这种远程调用方式，我们唯一要做的就是使用 OAuth2RestTemplate 替换原有的 RestTemplate，所有关于 Token 传播的细节已经被完整地封装在每次请求中。</p>
<h3>小结与预告</h3>
<p>这一讲我们的关注点在于对服务访问进行授权。通过今天的学习，我们明确了在微服务中嵌入访问授权控制的三种粒度。同时，在微服务系统中，因为涉及多个服务之间的交互，所以需要实现 Token 在这些服务之间的有效传播，我们可以借助 Spring Security 提供的工具类轻松实现这些需求。</p>
<p>本讲内容总结如下：
<img src="assets/CioPOWDwBviAFEsOAAE_BMghR5U884.jpg" alt="资源保护：如何基于 OAuth2 协议配置授权过程？.png" /></p>
<p>最后给你留一道思考题：你能描述对服务访问进行授权的三种层级，以及每个层级对应的实现方法吗？欢迎在留言区分享你的学习收获。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="13&#32;&#32;授权体系：如何构建&#32;OAuth2&#32;授权服务器？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="15&#32;&#32;令牌扩展：如何使用&#32;JWT&#32;实现定制化&#32;Token？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434dcfd95e70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
