<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>19  测试驱动：如何基于 Spring Security 测试系统安全性？.md</title>
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

                    <a class="current-tab" href="19&#32;&#32;测试驱动：如何基于&#32;Spring&#32;Security&#32;测试系统安全性？.md">19  测试驱动：如何基于 Spring Security 测试系统安全性？.md</a>
                    

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
                        <div><h1>19  测试驱动：如何基于 Spring Security 测试系统安全性？</h1>
<p>作为整个课程最后一部分内容，我们将讨论基于 Spring Security 的测试解决方案。对于安全性而言，测试是一个难点，也是经常被忽略的一套技术体系。当我们使用 Spring Security 时，如何验证我们所使用的安全性功能是否正确呢？今天的内容将给出详细的答案。</p>
<h3>如何对系统的安全性进行测试？</h3>
<p>Spring Security 是一款安全性开发框架，提供的是内嵌到业务系统中的基础设施类功能。因此，势必会涉及大量组件之间的依赖关系，这是测试安全性功能所面临的最大挑战，需要采用特定的测试方法。因此，在介绍具体的测试用例之前，我们先来梳理一下安全性测试方法，以及 Spring Security 中为我们提供的测试解决方案。</p>
<h3>安全性测试与 Mock 机制</h3>
<p>正如前面提到的，验证安全性功能正确性的难点在于组件与组件之间的依赖关系，为了弄清楚这个关系，这里就需要引出测试领域非常重要的一个概念，即 Mock（模拟）。<strong>针对测试组件涉及的外部依赖，我们的关注点在于这些组件之间的调用关系，以及返回的结果或发生的异常等，而不是组件内部的执行过程</strong>。因此常见的技巧就是使用 Mock 对象来替代真实的依赖对象，从而模拟真实的调用场景。</p>
<p>我们以一个常见的三层 Web 服务架构为例来进一步解释 Mock 的实施方法。Controller 层会访问 Service 层，而 Service 层又会访问 Repository 层，我们对 Controller 层的端点进行验证时，就需要模拟 Service 层组件的功能。同样，对 Service 层组件进行测试时，也需要假定 Repository 层组件的结果是可以获取的，如下所示：</p>
<p><img src="assets/Cgp9HWD_wkmAWv3aAADg8flYF9Q967.jpg" alt="2.jpg" /></p>
<p>Web 服务中各层组件与 Mock 对象示意图</p>
<p>对于 Spring Security 而言，上图所展示的原理同样适用，例如我们可以通过模拟用户的方式来测试用户认证和授权功能的正确性。在本讲后面的内容中，我们会给出相关的代码示例。</p>
<h3>Spring Security 中的测试解决方案</h3>
<p>要想开展单元测试、集成测试以及基于 Mock 的测试，需要有一套完整的技术体系。和 Spring Boot 1.x 版本一样，Spring Boot 2.x 同样提供了针对测试的 spring-boot-starter-test 组件。在 Spring Boot 中集成该组件的方法就是在 pom 文件中添加如下依赖：</p>
<pre><code>&lt;dependency&gt;

     &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;

     &lt;artifactId&gt;spring-boot-starter-test&lt;/artifactId&gt;

     &lt;scope&gt;test&lt;/scope&gt;

&lt;/dependency&gt;
</code></pre>
<p>通过这个依赖，一系列组件被自动引入到了代码工程的构建路径中，包括 JUnit、JSON Path、AssertJ、Mockito、Hamcrest 等，这些测试组件都非常有用。同时，因为 Spring Boot 程序的入口是 Bootstrap 类，因此专门提供了一个 @SpringBootTest 注解来测试你的 Bootstrap 类。所有配置都会通过 Bootstrap 类去加载，而该注解可以引用 Bootstrap 类的配置。</p>
<p>另一方面，Spring Security 也提供了专门用于测试安全性功能的 spring-security-test 组件，如下所示：</p>
<pre><code>&lt;dependency&gt;

     &lt;groupId&gt;org.springframework.security&lt;/groupId&gt;

     &lt;artifactId&gt;spring-security-test&lt;/artifactId&gt;

     &lt;scope&gt;test&lt;/scope&gt;

&lt;/dependency&gt;
</code></pre>
<p>该组件提供了相关的注解来模拟用户登录信息或者调用用户登录的方法，让我们一起来看一下。</p>
<h3>测试 Spring Security 功能</h3>
<h4>测试用户</h4>
<p>在使用 Spring Security 时，首先需要测试的无疑是合法的用户。假设我们实现了如下所示的一个简单 Controller：</p>
<pre><code>@RestController

public class HelloController {

 

    @GetMapping(&quot;/hello&quot;)

    public String hello() {

        return &quot;Hello&quot;;

    }

}
</code></pre>
<p>一旦我们启用 Spring Security 认证功能，那么对上述“/hello”端点就可以执行两种测试，分别面向认证和非认证用户。我们先来看一下针对非认证用户的测试方法：</p>
<pre><code>@SpringBootTest

@AutoConfigureMockMvc

public class HelloControllerTests {

 

    @Autowired

    private MockMvc mvc;

 

    @Test

    public void testUnauthenticatedUser() throws Exception {

        mvc.perform(get(&quot;/hello&quot;))

                .andExpect(status().isUnauthorized());

	}

}
</code></pre>
<p>这里引入了一个 @AutoConfigureMockMvc 注解，通过将 @SpringBootTest 注解与 @AutoConfigureMockMvc 注解相结合，@AutoConfigureMockMvc 注解在通过 @SpringBootTest 加载的 Spring 上下文环境中会自动装配 MockMvc 这个测试工具类。</p>
<p>顾名思义，MockMvc 用来对 WebMVC 的执行过程进行模拟。MockMvc 类提供的基础方法如下所示。</p>
<ul>
<li>perform：执行一个 RequestBuilder 请求，会自动执行 SpringMVC 流程，并映射到相应的 Controller 进行处理。</li>
<li>get/post/put/delete：声明发送一个 HTTP 请求的方式，根据 URI 模板和 URI 变量值得到一个 HTTP 请求，支持 GET、POST、PUT、DELETE 等 HTTP 方法。</li>
<li>param：添加请求参数，发送 JSON 数据时将不能使用这种方式，而应该采用 @ResponseBody 注解。</li>
<li>andExpect：添加 ResultMatcher 验证规则，通过对返回的数据进行判断来验证 Controller 执行结果是否正确。</li>
<li>andDo：添加 ResultHandler 结果处理器，比如调试时打印结果到控制台。</li>
<li>andReturn：最后返回相应的 MvcResult，然后执行自定义验证或做异步处理。</li>
</ul>
<p>在上述代码示例中，我们通过 perform、accept 和 andExpect 方法最终模拟 HTTP 请求的整个过程并验证请求的返回状态是否为非认证。</p>
<p>接下来我们来模拟认证用户的测试场景，测试用例如下所示：</p>
<pre><code>@Test

@WithMockUser

public void testAuthenticatedUser() throws Exception {

    mvc.perform(get(&quot;/hello&quot;))

           .andExpect(content().string(&quot;Hello&quot;))

           .andExpect(status().isOk());

}
</code></pre>
<p>显然，我们在这里看到了一个新的 @WithMockUser 注解，请注意这个注解是 Spring Security 所提供的，专门用来模拟认证用户。现在，既然已经有了认证用户，那么我们就可以验证响应的返回值以及状态，正如上述代码所示。</p>
<p>通过 @WithMockUser 注解，我们还可以指定用户的详细信息，例如如下所示的代码模拟了一个用户名为“admin”、角色为“USER”和“ADMIN”的认证用户：</p>
<pre><code>@WithMockUser(username=&quot;admin&quot;,roles={&quot;USER&quot;,&quot;ADMIN&quot;})
</code></pre>
<p>进一步，我们还可以通过模拟 UserDetailsService 来提供自定义的 UserDetails 用户信息。为此，Spring Security 中专门提供了一个 @WithUserDetails 注解，示例代码如下所示：</p>
<pre><code>@Test

@WithUserDetails(&quot;jianxiang&quot;)

public void testAuthenticatedUser() throws Exception {

    mvc.perform(get(&quot;/hello&quot;))

           .andExpect(content().string(&quot;Hello&quot;))

           .andExpect(status().isOk());

}
</code></pre>
<h4>测试认证</h4>
<p>测试完用户，我们接着来测试针对用户的认证过程。为了对整个认证过程有更多的定制化实现，这里专门提供一个 AuthenticationProvider 接口的实现类 MyAuthenticationProvider，如下所示：</p>
<pre><code>@Component

public class MyAuthenticationProvider implements AuthenticationProvider {

 

    @Override

    public Authentication authenticate(Authentication authentication) throws AuthenticationException {

        String username = authentication.getName();

        String password = String.valueOf(authentication.getCredentials());

 

        if (&quot;jianxiang&quot;.equals(username) &amp;&amp; &quot;123456&quot;.equals(password)) {

            return new UsernamePasswordAuthenticationToken(username, password, Arrays.asList());

        } else {

            throw new AuthenticationCredentialsNotFoundException(&quot;Error!&quot;);

        }

    }

 

    @Override

    public boolean supports(Class&lt;?&gt; authenticationType) {

        return UsernamePasswordAuthenticationToken.class.isAssignableFrom(authenticationType);

    }

}
</code></pre>
<p>现在，我们基于 HTTP 基础认证机制来编写测试用例，如下所示：</p>
<pre><code>@SpringBootTest

@AutoConfigureMockMvc

public class AuthenticationTests {

 

    @Autowired

    private MockMvc mvc;

 

    @Test

    public void testAuthenticatingWithValidUser() throws Exception {

        mvc.perform(get(&quot;/hello&quot;)

                .with(httpBasic(&quot;jianxiang&quot;,&quot;123456&quot;)))

                .andExpect(status().isOk());

    }

 

    @Test

    public void testAuthenticatingWithInvalidUser() throws Exception {

        mvc.perform(get(&quot;/hello&quot;)

                .with(httpBasic(&quot;noexiseduser&quot;,&quot;123456&quot;)))

                .andExpect(status().isUnauthorized());

    }

}
</code></pre>
<p>这里使用了前面介绍的 @AutoConfigureMockMvc 注解和 MockMvc 工具类，然后通过 httpBasic() 方法来实现 HTTP 基础认证。我们分别针对正确和错误的用户名/密码组合来执行 HTTP 请求并根据返回状态对认证结果进行校验。</p>
<h4>测试方法安全</h4>
<p>前面讨论的内容都是面向 Web 应用，也就是说测试的对象都是 HTTP 端点。那么，如何针对方法级别的安全性进行测试呢？</p>
<p>针对全局方法安全机制，前面介绍的 @WithMockUser 注解 @WithUserDetails 注解实际上也都是可以正常使用的。但因为已经脱离了 Web 环境，所以 MockMvc 工具类显然是无效的。这时候，你要做的事情就是在测试用例中直接注入目标方法即可，我们来看一下代码示例，假设一个非 Web 类的应用程序中存在如下一个 Service 类：</p>
<pre><code>@Service

public class HelloService {

 

    @PreAuthorize(&quot;hasAuthority('write')&quot;)

    public String hello() {

        return &quot;Hello&quot;;

    }

}
</code></pre>
<p>可以看到这里使用了 @PreAuthorize 注解限制了只有具备“write”权限的用户才能访问这个方法。</p>
<p>现在让我们编写针对方法访问安全的第一个测试用例，如下所示：</p>
<pre><code>@Autowired

private HelloService helloService;

 

@Test

void testMethodWithNoUser() {

      assertThrows(AuthenticationException.class,

           () -&gt; helloService.hello());

}
</code></pre>
<p>当我们在没有认证的情况下访问 helloService 的 hello() 方法，应该抛出一个 AuthenticationException 异常，上述测试用例验证了这一点。而如果我们使用一个具备不同权限的认证用户去访问这个方法时，会发生什么呢？对应测试用例如下所示：</p>
<pre><code>@Test

@WithMockUser(authorities = &quot;read&quot;)

void testMethodWithUserButWrongAuthority() {

     assertThrows(AccessDeniedException.class,

           () -&gt; helloService.hello());

}
</code></pre>
<p>可能看到这里使用了 @WithMockUser 模拟了一个具有“read”权限的认证用户，但因为 @PreAuthorize 注解中指定只有“write”权限的用户才能访问这个方法，所以会抛出一个 AccessDeniedException。</p>
<p>最后，我们来测试正常流程下的结果，测试用例如下所示：</p>
<pre><code>@Test

@WithMockUser(authorities = &quot;write&quot;)

void testMethodWithUserButCorrectAuthority() {

     Stringresult = helloService.hello();

 

     assertEquals(&quot;Hello&quot;, result);

}
</code></pre>
<h4>测试 CSRF 和 CORS 配置</h4>
<p>基于我们在[《攻击应对：如何实现 CSRF 保护和 CORS？》]中的讨论，对于 POST、PUT 和 DELETE 等 HTTP 请求，我们需要添加针对 CSRF 的安全保护。为了测试 CSRF 配置的正确性，假设我们存在这样一个 HTTP 端点，请注意它的 HTTP 方法是 POST：</p>
<pre><code>@RestController

public class HelloController {

 

    @PostMapping(&quot;/hello&quot;)

    public String postHello() {

        return &quot;Post Hello!&quot;;

    }

}
</code></pre>
<p>现在，我们通过 MockMvc 工具类发起 post 请求，测试用例如下所示：</p>
<pre><code>@Test

public void testHelloUsingPOST() throws Exception {

     mvc.perform(post(&quot;/hello&quot;))

            .andExpect(status().isForbidden());

}
</code></pre>
<p>请注意，这个 post 请求并没有携带 CSRF Token，所以响应的状态应该是 HTTP 403 Forbidden。</p>
<p>现在，让我们重构上述测试用例，如下所示：</p>
<pre><code>@Test

public void testHelloUsingPOSTWithCSRF() throws Exception {

     mvc.perform(post(&quot;/hello&quot;).with(csrf()))

            .andExpect(status().isOk());

}
</code></pre>
<p>上述 csrf() 方法的作用就是在请求中添加 CSRF Token，显然，这时候的响应结果应该是正确的。</p>
<p>讨论完 CSRF，我们再来看 CORS。在[《攻击应对：如何实现 CSRF 保护和 CORS？》]中，我们已经通过 CorsConfiguration 设置了 HTTP 响应消息头，如下所示：</p>
<pre><code>@Override

protected void configure(HttpSecurity http) throws Exception {

        http.cors(c -&gt; {

            CorsConfigurationSource source = request -&gt; {

                CorsConfiguration config = new CorsConfiguration();

                config.setAllowedOrigins(Arrays.asList(&quot;*&quot;));

                config.setAllowedMethods(Arrays.asList(&quot;*&quot;));

                return config;

            };

            c.configurationSource(source);

        });

        …

}
</code></pre>
<p>对上述配置进行测试的方法也很简单，我们通过 MockMvc 发起请求，然后对响应的消息头进行验证即可，测试用例如下所示：</p>
<pre><code>@SpringBootTest

@AutoConfigureMockMvc

public class MainTests {

 

    @Autowired

    private MockMvc mvc;

 

    @Test

    public void testCORSForTestEndpoint() throws Exception {

        mvc.perform(options(&quot;/hello&quot;)

                .header(&quot;Access-Control-Request-Method&quot;, &quot;POST&quot;)

                .header(&quot;Origin&quot;, &quot;http://www.test.com&quot;)

        )

        .andExpect(header().exists(&quot;Access-Control-Allow-Origin&quot;))

        .andExpect(header().string(&quot;Access-Control-Allow-Origin&quot;, &quot;*&quot;))

        .andExpect(header().exists(&quot;Access-Control-Allow-Methods&quot;))

        .andExpect(header().string(&quot;Access-Control-Allow-Methods&quot;, &quot;POST&quot;))

        .andExpect(status().isOk());

    }

}
</code></pre>
<p>可以看到，针对 CORS 配置，我们分别获取了响应结果的&quot;Access-Control-Allow-Origin&quot;和&quot;Access-Control-Allow-Methods&quot;消息头并进行了验证。</p>
<h3>小结与预告</h3>
<p>对于一个应用程序而言，无论其表现形式是否是一个 Web 服务，我们都需要对其进行安全性测试，为此 Spring Security 也提供了专门的测试解决方案，这其中很大程度上依赖于对 Mock 机制的合理应用。本讲对 Spring Security 所提供的用户、认证、全局方法、CSRF 以及 CORS 设计了测试用例，并给出了对应的示例代码。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="18&#32;&#32;技术趋势：如何为&#32;Spring&#32;Security&#32;添加响应式编程特性？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="20&#32;结束语&#32;&#32;以终为始，Spring&#32;Security&#32;的学习总结.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434deccff670ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
