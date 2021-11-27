<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>17 Sentinel 主流框架适配.md</title>
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

                    
                    <a href="01&#32;开篇词：一次服务雪崩问题排查经历.md">01 开篇词：一次服务雪崩问题排查经历.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;为什么需要服务降级以及常见的几种降级方式.md">02 为什么需要服务降级以及常见的几种降级方式.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;为什么选择&#32;Sentinel，Sentinel&#32;与&#32;Hystrix&#32;的对比.md">03 为什么选择 Sentinel，Sentinel 与 Hystrix 的对比.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;Sentinel&#32;基于滑动窗口的实时指标数据统计.md">04 Sentinel 基于滑动窗口的实时指标数据统计.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;Sentinel&#32;的一些概念与核心类介绍.md">05 Sentinel 的一些概念与核心类介绍.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;Sentinel&#32;中的责任链模式与&#32;Sentinel&#32;的整体工作流程.md">06 Sentinel 中的责任链模式与 Sentinel 的整体工作流程.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;Java&#32;SPI&#32;及&#32;SPI&#32;在&#32;Sentinel&#32;中的应用.md">07 Java SPI 及 SPI 在 Sentinel 中的应用.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;资源指标数据统计的实现全解析（上）.md">08 资源指标数据统计的实现全解析（上）.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;资源指标数据统计的实现全解析（下）.md">09 资源指标数据统计的实现全解析（下）.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;限流降级与流量效果控制器（上）.md">10 限流降级与流量效果控制器（上）.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;限流降级与流量效果控制器（中）.md">11 限流降级与流量效果控制器（中）.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;限流降级与流量效果控制器（下）.md">12 限流降级与流量效果控制器（下）.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;熔断降级与系统自适应限流.md">13 熔断降级与系统自适应限流.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;黑白名单限流与热点参数限流.md">14 黑白名单限流与热点参数限流.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;自定义&#32;ProcessorSlot&#32;实现开关降级.md">15 自定义 ProcessorSlot 实现开关降级.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;Sentinel&#32;动态数据源：规则动态配置.md">16 Sentinel 动态数据源：规则动态配置.md</a>

                </li>
                <li>

                    <a class="current-tab" href="17&#32;Sentinel&#32;主流框架适配.md">17 Sentinel 主流框架适配.md</a>
                    

                </li>
                <li>

                    
                    <a href="18&#32;Sentinel&#32;集群限流的实现（上）.md">18 Sentinel 集群限流的实现（上）.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;Sentinel&#32;集群限流的实现（下）.md">19 Sentinel 集群限流的实现（下）.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;结束语：Sentinel&#32;对应用的性能影响如何？.md">20 结束语：Sentinel 对应用的性能影响如何？.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;番外篇：Sentinel&#32;1.8.0&#32;熔断降级新特性解读.md">21 番外篇：Sentinel 1.8.0 熔断降级新特性解读.md</a>

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
                        <div><h1>17 Sentinel 主流框架适配</h1>
<p>使用 Sentinel 需要用 try-catch-finally 将需要保护的资源（方法或者代码块）包装起来，在目标方法或者代码块执行之前，调用 ContextUtil#enter 方法以及 SphU#entry 方法，在抛出异常时，如果非 BlockException 异常需要调用 Tracer#trace 记录异常，修改异常指标数据，在 finally 中需要调用 Entry#exit 方法，以及 ContextUtil#exit 方法。</p>
<p>为了节省这些步骤，Sentinel 提供了对主流框架的适配，如适配 Spring MVC、Webflux、Dubbo、Api Gateway 等框架。当然，对于 Sentinel 未适配的框架，我们也可以自己实现适配器。在 Sentinel 源码之外，alibaba 的 spring-cloud-starter-alibaba-sentinel 也为 Sentinel 提供与 OpenFeign 框架整合的支持。</p>
<p><img src="assets/ae715de0-ed3b-11ea-be9c-f7616f01fc23" alt="17-01-sentinel-adapter" /></p>
<h3>Spring MVC 适配器</h3>
<p>Sentinel 借助 Spring MVC 框架的 HandlerInterceptor 适配 Spring MVC，但也需要我们借助 WebMvcConfigurer 将 SentinelWebInterceptor 注册到 Spring MVC 框架。</p>
<h4><strong>使用步骤</strong></h4>
<p>第一步：在项目中添加 Spring MVC 适配模块的依赖。</p>
<pre><code>&lt;dependency&gt;
    &lt;groupId&gt;com.alibaba.csp&lt;/groupId&gt;
    &lt;artifactId&gt;sentinel-spring-webmvc-adapter&lt;/artifactId&gt;
    &lt;version&gt;${version}&lt;/version&gt;
&lt;/dependency&gt;

</code></pre>
<p>第二步：编写 WebMvcConfigurer，在 addInterceptors 方法中注入 SentinelWebInterceptor。</p>
<pre><code class="language-java">@Configuration
public class InterceptorConfig implements WebMvcConfigurer {
    @Override
    public void addInterceptors(InterceptorRegistry registry) {
        SentinelWebMvcConfig config = new SentinelWebMvcConfig();
        config.setBlockExceptionHandler(new DefaultBlockExceptionHandler());
        config.setHttpMethodSpecify(true);
        config.setOriginParser(request -&gt; request.getHeader(&quot;S-user&quot;));
        // SentinelWebInterceptor 拦截所有接口（&quot;/**&quot;）
        registry.addInterceptor(new SentinelWebInterceptor(config)).addPathPatterns(&quot;/**&quot;);
    }
}

</code></pre>
<p>在创建 SentinelWebInterceptor 时，可为 SentinelWebInterceptor 添加配置，使用 SentinelWebMvcConfig 封装这些配置：</p>
<ul>
<li>setBlockExceptionHandler：配置 BlockException 异常处理器，如果不想配置 BlockException 异常处理器，也可在 Spring MVC 的全局异常处理器中处理 BlockException 异常。</li>
<li>setOriginParser：注册调用来源（origin）解析器，例如从请求头中获取“S-user”参数的值作为调用来源名称，上游服务在发起请求时就可在请求头写入“S-user”参数告知自己的身份。</li>
<li>setHttpMethodSpecify：是否需要给资源名称加上 HttpMethod 前缀，例如 GET 接口“/hello”，如果 httpMethodSpecify 配置为 false，则资源名称为“/hello”，否则资源名称为“GET:/hell”。</li>
</ul>
<h4><strong>适配原理</strong></h4>
<p>Spring MVC 框架的方法拦截器（HandlerInterceptor）的定义如下：</p>
<pre><code class="language-java">public interface HandlerInterceptor {
    default boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
        return true;
    }
    default void postHandle(HttpServletRequest request, HttpServletResponse response, Object handler, @Nullable ModelAndView modelAndView) throws Exception {
    }
    default void afterCompletion(HttpServletRequest request, HttpServletResponse response, Object handler, @Nullable Exception ex) throws Exception {
    }
}

</code></pre>
<p>HandlerInterceptor 在 DispatcherServlet#doDispatch 方法中被调用，每个方法的调用时机如下：</p>
<ul>
<li>preHandle：在调用接口方法之前调用</li>
<li>postHandle：在接口方法执行完成返回 ModelAndView 时被调用；</li>
<li>afterCompletion：在接口方法执行完成时被调用，无论成功或异常都会被调用；</li>
</ul>
<p>因此，Sentinel 可借助 HandlerInterceptor 与 Spring MVC 框架整合，在 HandlerInterceptor#preHandle 方法中调用 ContextUtil#enter 方法以及 SphU#entry 方法，在 afterCompletion 方法中根据方法参数 ex 是否为空处理异常情况，并且完成 Entry#exit 方法、ContextUtil#exit 方法的调用。</p>
<p>SentinelWebInterceptor 是 AbstractSentinelInterceptor 的子类，preHandle 与 afterCompletion 方法在父类中实现，自身只实现父类定义的一个获取资源名称的抽象方法，其源码如下：</p>
<pre><code class="language-java">    @Override
    protected String getResourceName(HttpServletRequest request) {
        // （1）
        Object resourceNameObject = request.getAttribute(HandlerMapping.BEST_MATCHING_PATTERN_ATTRIBUTE);
        if (resourceNameObject == null || !(resourceNameObject instanceof String)) {
            return null;
        }
        String resourceName = (String) resourceNameObject;
        // （2）
        UrlCleaner urlCleaner = config.getUrlCleaner();
        if (urlCleaner != null) {
            resourceName = urlCleaner.clean(resourceName);
        }
        // （3）
        if (StringUtil.isNotEmpty(resourceName) &amp;&amp; config.isHttpMethodSpecify()) {
            resourceName = request.getMethod().toUpperCase() + &quot;:&quot; + resourceName;
        }
        return resourceName;
    }

</code></pre>
<p>资源名称生成过程如下。</p>
<p>\1. 从 HttpServletRequest 的属性中获取 HandlerMapping 匹配的 URL。</p>
<p>因为有些接口是这样的：“/hello/{name}”，如果直接从 HttpServletRequest 获取请求路径，那么每个请求获取到的 URL 就可能会不同。</p>
<p>\2. 如果 UrlCleaner 不为空，则调用 UrlCleaner 的 clean 方法。</p>
<p>UrlCleaner 用于实现将多个接口合并为一个，例如接口：“/user/create”、“/user/del”、“/user/update”，借助 UrlCleaner 修改资源名称将这几个接口都改为“/user/**”即可实现三个接口使用同一个限流规则。</p>
<p>\3. 根据 SentinelWebMvcConfig 配置对象判断是否需要添加 HttpMethod 前缀，如果需要则给资源名称拼接前缀。</p>
<p>一般来说，不建议使用，因为如果接口使用 @RequestMapping 声明，那么想对该接口限流就需要配置多个限流规则，而一般旧项目多是使用 @RequestMapping 声明接口方法。例如接口“/user/create”，你可能需要针对“GET:/user/create”、“POST:/user/create”等多个资源配置限流规则。</p>
<p>由于 AbstractSentinelInterceptor 的源码较多，我们分几个步骤分析。</p>
<p>AbstractSentinelInterceptor#preHandle 方法源码如下：</p>
<pre><code class="language-java">    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler)
        throws Exception {
        try {
            //（1）
            String resourceName = getResourceName(request);
            if (StringUtil.isNotEmpty(resourceName)) {
                //（2）
                String origin = parseOrigin(request);
                //（3）
                ContextUtil.enter(SENTINEL_SPRING_WEB_CONTEXT_NAME, origin);
                //（4）
                Entry entry = SphU.entry(resourceName, ResourceTypeConstants.COMMON_WEB, EntryType.IN);
                //（5）
                setEntryInRequest(request, baseWebMvcConfig.getRequestAttributeName(), entry);
            }
            return true;
        } catch (BlockException e) {
            // （6）
            handleBlockException(request, response, e);
            return false;
        }
    }

</code></pre>
<ol>
<li>获取资源名称；</li>
<li>调用 OriginParser#parseOrigin 方法解析调用来源，例如从请求头获取&quot;S-user&quot;参数的值；</li>
<li>调用 ContextUtil#enter 方法，Context 名称为“sentinel_spring_web_context”；</li>
<li>调用 SphU#entry 方法，资源类型为 COMMON_WEB，流量类型为 IN；</li>
<li>将 SphU#entry 方法返回的 Entry 放入 HttpServletRequest 的属性表中，方便在 afterCompletion 中取出；</li>
<li>如果抛出 BlockException 异常，说明当前请求被拒绝，需调用 handleBlockException 方法处理 BlockException 异常。</li>
</ol>
<p>AbstractSentinelInterceptor#handleBlockException 方法源码如下：</p>
<pre><code class="language-java">protected void handleBlockException(HttpServletRequest request, HttpServletResponse response, BlockException e)
        throws Exception {
        if (baseWebMvcConfig.getBlockExceptionHandler() != null) {
            baseWebMvcConfig.getBlockExceptionHandler().handle(request, response, e);
        } else {
            throw e;
        }
    }

</code></pre>
<p>如果我们给 SentinelWebMvcConfig 配置了 BlockExceptionHandler，则调用 BlockExceptionHandler#handle 方法处理 BlockException 异常，否则将异常抛出，由全局处理器处理。</p>
<p>AbstractSentinelInterceptor#afterCompletion 方法源码如下：</p>
<pre><code class="language-java">    @Override
    public void afterCompletion(HttpServletRequest request, HttpServletResponse response,
                                Object handler, Exception ex) throws Exception {
        //（1）
        Entry entry = getEntryInRequest(request, baseWebMvcConfig.getRequestAttributeName());
        if (entry != null) {
            //（2）
            traceExceptionAndExit(entry, ex);
            removeEntryInRequest(request);
        }
        //（3）
        ContextUtil.exit();
    }

</code></pre>
<ol>
<li>从 HttpServletRequest 的属性表中获取 preHandle 方法放入的 Entry；</li>
<li>调用 traceExceptionAndExit 方法，记录异常和调用 Entry#exit 方法；</li>
<li>调用 ContextUtil#exit 方法，如果当前 CtEntry 为空，则从 ThreadLocal 中移除 Context。</li>
</ol>
<p>AbstractSentinelInterceptor#traceExceptionAndExit 方法源码如下：</p>
<pre><code class="language-java">   protected void traceExceptionAndExit(Entry entry, Exception ex) {
        if (entry != null) {
            if (ex != null) {
                Tracer.traceEntry(ex, entry);
            }
            entry.exit();
        }
    }

</code></pre>
<p>当方法执行抛出异常时，调用 Tracer#traceEntry 方法记录异常，更新异常指标数据。</p>
<h3>OpenFeign 适配器</h3>
<p>Sentinel 整合 OpenFeign 主要用于实现熔断降级，因此，关于 OpenFeign 的 Sentinel 适配器的使用介绍基于服务消费端。</p>
<h4><strong>使用步骤</strong></h4>
<p><strong>1. 引入依赖</strong></p>
<p>借助 spring-cloud-starter-alibaba-sentinel 实现与 OpenFeign 整合，添加依赖配置如下：</p>
<pre><code class="language-xml">&lt;dependency&gt;
    &lt;groupId&gt;com.alibaba.cloud&lt;/groupId&gt;
    &lt;artifactId&gt;spring-cloud-starter-alibaba-sentinel&lt;/artifactId&gt;
    &lt;version&gt;2.2.1.RELEASE&lt;/version&gt;
&lt;/dependency&gt;

</code></pre>
<p><strong>2. 启用 OpenFeign 整合 Sentinel 的自动配置</strong></p>
<p>在 application.yaml 配置文件中添加如下配置，启用 Sentinel 与 OpenFeign 整合适配器。</p>
<pre><code class="language-yaml">feign:
  sentinel:
    enabled: true

</code></pre>
<p><strong>3. 熔断降级规则配置</strong></p>
<p>可基于动态数据源实现，也可直接调用 DegradeRuleManager 的 loadRules API 硬编码实现，可参考上一篇。</p>
<p><strong>4. 给 @FeignClient 注解配置异常回调</strong></p>
<p>给接口上的 @FeignClient 注解配置 fallback 属性，实现请求被拒绝后的处理。</p>
<pre><code class="language-java">@FeignClient(
         //.....
        // 这里配置
        fallback = ServiceDegradeFallback.class)
public interface DemoService {

    @PostMapping(&quot;/services&quot;)
    ListGenericResponse&lt;DemoDto&gt; getServices();

}

</code></pre>
<p>fallback 属性要求配置一个类，该类必须实现相同的接口，所以 ServiceDegradeFallback 必须实现 DemoService 接口。</p>
<pre><code class="language-java">public class ServiceDegradeFallback implements DemoService {
    @Override
    public ListGenericResponse&lt;DemoDto&gt; getServices() {
        ListGenericResponse response = new ListGenericResponse&lt;DemoDto&gt;();
        response.setCode(ResultCode.SERVICE_DEGRAD.getCode())
                .setMessage(&quot;服务降级&quot;);
        return response;
    }
}

</code></pre>
<p>ServiceDegradeFallback 类中处理接口降级逻辑，例如，响应一个状态码告知消费端由于服务降级本次接口调用失败。</p>
<p>最后还需要将该 ServiceDegradeFallback 注册到 Feign 的 Clinet 环境隔离的容器中。</p>
<p>编写配置类 SentinelFeignConfig，在 SentinelFeignConfig 中注册 ServiceDegradeFallback。</p>
<pre><code class="language-java">public class SentinelFeignConfig {
    @Bean
    public ServiceDegradeFallback degradeMockYcpayService() {
        return new ServiceDegradeFallback();
    }
}

</code></pre>
<p>将 SentinelFeignConfig 配置类添加到 @FeignClient 注解的 configuration 属性，如下：</p>
<pre><code class="language-java">@FeignClient(
        // .....
        configuration = {
                // 这里配置
                SentinelFeignConfig.class
        },
        // 这里配置
        fallback = ServiceDegradeFallback.class)
public interface DemoService {

    @PostMapping(&quot;/services&quot;)
    ListGenericResponse&lt;DemoDto&gt; getServices();

}

</code></pre>
<p>当满足熔断条件时，Sentinel 会抛出一个 DegradeException 异常，如果配置了 fallback，那么 Sentinel 会从 Bean 工厂中根据 fallback 属性配置的类型取一个 Bean 并调用接口方法。</p>
<h4><strong>Sentinel 与 OpenFeign 整合实现原理</strong></h4>
<p>当 Sentinel 与 OpenFeign、Ribbon 整合时，客户端向服务端发起一次请求的过程如下图所示。</p>
<p><img src="assets/7b545840-ed3b-11ea-9210-e5c7b119b96e" alt="17-02-openfeign-sentinel" /></p>
<ol>
<li>当调用@FeignClient 接口的方法时，由 Sentinel 提供的方法调用拦截器（SentinelInvocationHandler）拦截方法的执行，根据接口方法上注解的 url 生成资源名称，然后调用 Sentinel 的 SphU#entry 方法（完成所有 ProcessorSlot#entry 方法的调用），判断当前发起的请求是否需要熔断；</li>
<li>非熔断降级情况下，继续将请求交给 OpenFeign 的 MethodHandler 处理；</li>
<li>OpenFeign 从 Ribbon 获取一个服务提供者节点；</li>
<li>OpenFeign 使用 HttpClient 发起 HTTP 请求；</li>
<li>OpenFeign 请求成功或者异常（已经经过重试）时，调用 Sentinel 的 Entry#exit 方法（完成所有 ProcessorSlot#exit 方法的调用）更新当前时间窗口的请求成功总数、异常总数等指标数据。</li>
</ol>
<p>可见，Sentinel 处在接口调用的最前端，因此 Sentinel 统计的指标数据即不会受 Ribbon 的重试影响也不会受 OpenFeign 的重试影响。</p>
<p>Sentinel 通过自己提供 InvocationHandler 替换 OpenFeign 的 InvocationHandler 实现请求拦截。SentinelInvocationHandler 源码调试如下图所示。</p>
<p><img src="assets/d7b506c0-ed3b-11ea-816b-87f82de6664d" alt="17-02-openfeign-sentinel02" /></p>
<p>InvocationHandler 是 OpenFeign 为接口生成 JDK 动态代理类时所需要的，是接口的方法拦截处理器，Sentinel 通过替换 OpenFeign 的 InvocationHandler 拦截方法的执行，在 OpenFeign 处理接口调用之前完成熔断降级的检查。</p>
<p>那么，Sentinel 是如何将原本的 FeignInvocationHandler 替换为 SentinelInvocationHandler 的呢？</p>
<p>OpenFeign 通过 Feign.Builder 类创建接口的代理类，所以 Sentinel 直接将 Feign.Builder 也替换成了 SentinelFeign.Builder，由 SentinelFeignAutoConfiguration 自动配置类向 Spring 的 Bean 容器注入 SentinelFeign.Builder，代码如下：</p>
<pre><code class="language-java">@Configuration(proxyBeanMethods = false)
@ConditionalOnClass({ SphU.class, Feign.class })
public class SentinelFeignAutoConfiguration {

    @Bean
    @Scope(&quot;prototype&quot;)
    @ConditionalOnMissingBean
    @ConditionalOnProperty(name = &quot;feign.sentinel.enabled&quot;)
    public Feign.Builder feignSentinelBuilder() {
        return SentinelFeign.builder();
    }

}

</code></pre>
<p>SentinelFeign.Builder 继承 Feign.Builder 并重写 build 方法，SentinelFeign.Builder#build 方法源码如下：</p>
<pre><code class="language-java">public final class SentinelFeign {

    public static Builder builder() {
        return new Builder();
    }

    public static final class Builder extends Feign.Builder
            implements ApplicationContextAware {

       // .....

        @Override
        public Feign build() {
            super.invocationHandlerFactory(new InvocationHandlerFactory() {
                @Override
                public InvocationHandler create(Target target,
                        Map&lt;Method, MethodHandler&gt; dispatch) {
                    // 创建 SentinelInvocationHandler
                }
            });
            super.contract(new SentinelContractHolder(contract));
            return super.build();
        }
        // .....
    }

}

</code></pre>
<p>SentinelFeign.Builder#build 偷天换日，替换了 InvocationHandlerFactory，所以 OpenFeign 调用 InvocationHandlerFactory#create 方法创建的 InvocationHandler 就变成了 SentinelInvocationHandler。</p>
<p>看 InvocationHandlerFactory#create 方法的返回值类型我们也能知道，该方法负责创建 SentinelInvocationHandler。create 方法部分源码如下：</p>
<pre><code class="language-java">Class fallback = (Class) getFieldValue(feignClientFactoryBean,
                            &quot;fallback&quot;);
Object fallbackInstance = getFromContext(beanName, &quot;fallback&quot;, fallback,
                                target.type());
return new SentinelInvocationHandler(target, dispatch,
                                new FallbackFactory.Default(fallbackInstance));

</code></pre>
<p>在创建 SentinelInvocationHandler 之前，通过反射从 FeignClientFactoryBean 拿到 @FeignClient 注解的 fallback 属性值，然后根据 fallback 类型从 Bean 工厂取得 fallback 实例，将 fallback 实例传递给 SentinelInvocationHandler。当触发熔断时，SentinelInvocationHandler 就能取得 fallback 实例并调用。</p>
<h3>总结</h3>
<p>本篇我们分析了 Sentinel 适配 Spring MVC 框架的实现原理，以及 Sentinel 适配 Spring Cloud OpenFeign 框架的实现原理。适配各种主流框架，无非就是通过框架提供的方法拦截器注入 Sentinel，或者通过拦截主流框架的入口方法注入 Sentinel。了解原理之后，如果我们项目中使用的框架 Sentinel 并未适配，那么我们也可以自己实现适配器。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="16&#32;Sentinel&#32;动态数据源：规则动态配置.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="18&#32;Sentinel&#32;集群限流的实现（上）.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b435986e99f645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/%E6%B7%B1%E5%85%A5%E7%90%86%E8%A7%A3%20Sentinel%EF%BC%88%E5%AE%8C%EF%BC%89/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
