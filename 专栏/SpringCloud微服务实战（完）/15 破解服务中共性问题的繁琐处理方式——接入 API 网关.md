<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>15 破解服务中共性问题的繁琐处理方式——接入 API 网关.md</title>
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

                    
                    <a href="00&#32;开篇导读.md">00 开篇导读.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;以真实“商场停车”业务切入——需求分析.md">01 以真实“商场停车”业务切入——需求分析.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;具象业务需求再抽象分解——系统设计.md">02 具象业务需求再抽象分解——系统设计.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;第一个&#32;Spring&#32;Boot&#32;子服务——会员服务.md">03 第一个 Spring Boot 子服务——会员服务.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;如何维护接口文档供外部调用——在线接口文档管理.md">04 如何维护接口文档供外部调用——在线接口文档管理.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;认识&#32;Spring&#32;Cloud&#32;与&#32;Spring&#32;Cloud&#32;Alibaba&#32;项目.md">05 认识 Spring Cloud 与 Spring Cloud Alibaba 项目.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;服务多不易管理如何破——服务注册与发现.md">06 服务多不易管理如何破——服务注册与发现.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;如何调用本业务模块外的服务——服务调用.md">07 如何调用本业务模块外的服务——服务调用.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;服务响应慢或服务不可用怎么办——快速失败与服务降级.md">08 服务响应慢或服务不可用怎么办——快速失败与服务降级.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;热更新一样更新服务的参数配置——分布式配置中心.md">09 热更新一样更新服务的参数配置——分布式配置中心.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;如何高效读取计费规则等热数据——分布式缓存.md">10 如何高效读取计费规则等热数据——分布式缓存.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;多实例下的定时任务如何避免重复执行——分布式定时任务.md">11 多实例下的定时任务如何避免重复执行——分布式定时任务.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;同一套服务如何应对不同终端的需求——服务适配.md">12 同一套服务如何应对不同终端的需求——服务适配.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;采用消息驱动方式处理扣费通知——集成消息中间件.md">13 采用消息驱动方式处理扣费通知——集成消息中间件.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;Spring&#32;Cloud&#32;与&#32;Dubbo&#32;冲突吗——强强联合.md">14 Spring Cloud 与 Dubbo 冲突吗——强强联合.md</a>

                </li>
                <li>

                    <a class="current-tab" href="15&#32;破解服务中共性问题的繁琐处理方式——接入&#32;API&#32;网关.md">15 破解服务中共性问题的繁琐处理方式——接入 API 网关.md</a>
                    

                </li>
                <li>

                    
                    <a href="16&#32;服务压力大系统响应慢如何破——网关流量控制.md">16 服务压力大系统响应慢如何破——网关流量控制.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;集成网关后怎么做安全验证——统一鉴权.md">17 集成网关后怎么做安全验证——统一鉴权.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;多模块下的接口&#32;API&#32;如何统一管理——聚合&#32;API.md">18 多模块下的接口 API 如何统一管理——聚合 API.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;数据分库后如何确保数据完整性——分布式事务.md">19 数据分库后如何确保数据完整性——分布式事务.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;优惠券如何避免超兑——引入分布式锁.md">20 优惠券如何避免超兑——引入分布式锁.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;如何查看各服务的健康状况——系统应用监控.md">21 如何查看各服务的健康状况——系统应用监控.md</a>

                </li>
                <li>

                    
                    <a href="22&#32;如何确定一次完整的请求过程——服务链路跟踪.md">22 如何确定一次完整的请求过程——服务链路跟踪.md</a>

                </li>
                <li>

                    
                    <a href="23&#32;结束语.md">23 结束语.md</a>

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
                        <div><h1>15 破解服务中共性问题的繁琐处理方式——接入 API 网关</h1>
<p>由于服务粒度的不同以及数据包装因端而异的差异需求，我们在之前章节中引入了 BFF 层，调用端可以直接调用 BFF 层，由 BFF 层再将请求分发至不同微服务，进行数据组装。由于很多子服务都需要用户验证、权限验证、流量控制等，真的要在每个子服务中重复编写用户验证的逻辑吗？本章节就带你走近网关，在网关层统一处理这些共性需求。</p>
<h3>为什么引入网关</h3>
<p>如果没有网关的情况下，服务调用面临的几个直接问题：</p>
<ol>
<li>每个服务都需要独立的认证，增加不必要的重复度</li>
<li>客户端直接与服务对接，后端服务一旦变动，前端也要跟着变动，独立性缺失</li>
<li>将后端服务直接暴露在外，服务的安全性保障是一个挑战</li>
<li>某些公共的操作，如日志记录等，需要在每个子服务都实现一次，造成不必要的重复劳动</li>
</ol>
<p>现有系统的调用结构如下图所示：</p>
<p><img src="assets/6e3c7270-9b22-11ea-bcff-e5fb1076ab0f" alt="img" /></p>
<p>直接由前端发起调用，服务间的调用可以 由服务注册中心调配，但前端调用起来就没这么简单了，特别是后端服务以多实例的形态出现时。由于各个子服务都有各自的服务名、端口号等，加之某些共性的东西（如鉴权、日志、服务控制等）重复在各子模块实现，造成不必要的成本浪费。此时，就亟需一个网关，将所有子服务包装后，对外统一提供服务，并在网关层针对所有共性的功能作统一处理，大大提高服务的可维护性、健壮性。</p>
<p>引入网关后，请求的调用结构演变成如下图：</p>
<p><img src="assets/7d504f70-9b22-11ea-a470-713f9388c33a" alt="img" /></p>
<p>可以看到明显的变化：由网关层进行统一的请求路由，将前端调用的选择权解放出来；后端服务隐藏起来，对外只能看到网关的地址，安全性大大提升；一些共性操作，直接由网关层实现，具体服务实现不再承担这部分工作，更加专心于业务实现。</p>
<p>本文带你将 spring-cloud-gateway 组件引入项目中，有同学会问，为什么不用 Zuul 呢？答案是由于组件发展的一些原因，Zuul 进入了维护期，为保证组件的完整性，Spring 官方团队开发出 Gateway 以替代 Zuul 来实现网关功能。</p>
<h3>建立 Gateway 服务</h3>
<p>引入 jar 时，注意 Spring Cloud Gateway 是基于 Netty 和 WebFlux 开发，所以不需要相关的 Web Server 依赖，如 Tomcat 等，WebFlux 与 spring-boot-starter-web 是冲突的，需要将这两项排除，否则无法启动。</p>
<pre><code class="language-xml">&lt;dependency&gt;
            &lt;groupId&gt;org.springframework.cloud&lt;/groupId&gt;
            &lt;artifactId&gt;spring-cloud-starter-gateway&lt;/artifactId&gt;
&lt;/dependency&gt;
&lt;dependency&gt;
            &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
            &lt;artifactId&gt;spring-boot-starter-actuator&lt;/artifactId&gt;
&lt;/dependency&gt;
&lt;dependency&gt;
            &lt;groupId&gt;org.springframework.cloud&lt;/groupId&gt;
            &lt;artifactId&gt;spring-cloud-starter-alibaba-nacos-discovery&lt;/artifactId&gt;
            &lt;version&gt;0.2.2.RELEASE&lt;/version&gt;
&lt;/dependency&gt;

</code></pre>
<p>启动类与正常业务模块无异，在 application.yml 配置文件中进行初步配置：</p>
<pre><code class="language-yaml">server: 
  port: 10091

management: 
  endpoints: 
    web: 
      exposure: 
        include: '*'

#nacos config
spring: 
  application: 
    name: gateway-service
  cloud: 
    nacos: 
      discovery: 
        register-enabled: true
        server-addr: 127.0.0.1:8848
#      config: 
#        server-addr: 127.0.0.1:8848
    gateway: 
      discovery:
        locator:
          enabled: false  #gateway 开启服务注册和发现的功能，并且自动根据服务发现为每一个服务创建了一个 router，这个 router 将以服务名开头的请求路径转发到对应的服务。
          lowerCaseServiceId: true   #是将请求路径上的服务名配置为小写
          filters:
            - StripPrefix=1
      routes: 
      #一个服务中的 id、uri、predicates 是必输项
      #member 子服务
      - id: member-service
        uri: lb://member-service
        predicates: 
        - Path= /member/**
        filters: 
        - StripPrefix=1
      #card 子服务
      - id: card-service
        uri: lb://card-service
        predicates: 
        - Path=/card/**
        filters:
        - StripPrefix=1
      #resource 子服务
      - id: resource-service
        uri: lb://resource-service
        predicates: 
        - Path=/resources/**
        filters:
        - StripPrefix=1
      #计费子服务
      - id: charging-service
        uri: lb://charging-service
        predicates: 
        - Path=/charging/**
        filters: 
        - StripPrefix=1
      #finance 子服务
      - id: finance-service
        uri: lb://finance-service
        predicates: 
        - Path=/finance/**
        filters: 
        - StripPrefix=1

</code></pre>
<p>routes 配置项是具体的服务路由规则配置，各服务以数组形式配置。id 用于服务间的区分，uri 则对应直接的调用服务，lb 表示以负载的形式访问服务，lb 后面配置的是 Nacos 中的服务名。predicates 用于匹配请求，无须再用服务的形式访问。</p>
<p>到此完成 Gateway 网关服务的简单路由功能已完成，前端直接访问网关调用对应服务，不必再关心子服务的服务名、服务端口等情况。</p>
<h3>熔断降级</h3>
<p>有服务调用章节，我们通过 Hystrix 实现了服务降级，在网关层面是不是可以做一个统一配置呢？答案是肯定的，下面我们在 Gateway 模块中引入 Hystrix 来进行服务设置，当服务超时或超过指定配置时，直接快速返回准备好的异常方法，快速失败，实现服务的熔断操作。</p>
<p>引入相关的 jar 包：</p>
<pre><code class="language-xml">        &lt;dependency&gt;
            &lt;groupId&gt;org.springframework.cloud&lt;/groupId&gt;
            &lt;artifactId&gt;spring-cloud-starter-netflix-hystrix&lt;/artifactId&gt;
        &lt;/dependency&gt;

</code></pre>
<p>配置文件中设置熔断超时时间设置：</p>
<pre><code class="language-yaml">#timeout time config，默认时间为 1000ms，
hystrix: 
  command: 
    default: 
      execution: 
        isolation: 
          thread: 
            timeoutInMilliseconds: 2000

</code></pre>
<p>编写异常响应类，此类需要配置在子服务的失败调用位置。</p>
<pre><code class="language-java">@RestController
@RequestMapping(&quot;error&quot;)
@Slf4j
public class FallbackController {

    @RequestMapping(&quot;/fallback&quot;)
    public CommonResult&lt;String&gt; fallback() {
        CommonResult&lt;String&gt; errorResult = new CommonResult&lt;&gt;(&quot;Invoke failed.&quot;);
        log.error(&quot;Invoke service failed...&quot;);
        return errorResult;
    }
}

      #card 子服务
      - id: card-service
        uri: lb://card-service
        predicates: 
        - Path=/card/**
        filters:
        - StripPrefix=1
        #配置快速熔断失败调用
        - name: Hystrix
          args: 
            name: fallbackcmd
            fallbackUri: forward:/error/fallback

</code></pre>
<p>若服务暂时不可用，发起重试后又能返回正常，可以通过设置重试次数，来确保服务的可用性。</p>
<pre><code class="language-yaml">      #card 子服务
      - id: card-service
        uri: lb://card-service
        predicates: 
        - Path=/card/**
        filters:
        - StripPrefix=1
        - name: Hystrix
          args: 
            name: fallbackcmd
            fallbackUri: forward:/error/fallback
        - name: Retry
          args: 
              #重试 3 次，加上初次访问，正确执行应当是 4 次访问
            retries: 3
            statuses: 
            - OK
            methods: 
            - GET
            - POST
            #异常配置，与代码中抛出的异常保持一致
            exceptions: 
            - com.mall.parking.common.exception.BusinessException

</code></pre>
<p>如何测试呢？可以代码中增加异常抛出，来测试请求是否重试 3 次，前端调用时，通过网关访问此服务调用，可以发现被调用次数是 4 次。</p>
<pre><code class="language-java">        /* 这里抛出异常是为了测试 spring-cloud-gateway 的 retry 机制是否正常运行
         * if (StringUtils.isEmpty(&quot;&quot;)) {
            throw new BusinessException(&quot;test retry function&quot;);
        }*/

</code></pre>
<h3>服务限流</h3>
<p>为什么要限流，当服务调用压力突然增大时，对系统的冲击是很大的，为保证系统的可用性，做一些限流措施很有必要。</p>
<p>常见的限流算法有令牌桶、漏桶等，Gateway 组件内部默认实现了 Redis + Lua 进行限流，可以通过自定义的方式来指定是根据 IP、用户或是 URI 来进行限流，下面我们来一控究竟。</p>
<p>Spring Cloud Gateway 默认提供的 RedisRateLimter 的核心逻辑为判断是否取到令牌的实现，通过调用 META-INF/scripts/request_rate_limiter.lua 脚本实现基于令牌桶算法限流，我们来看看如何借助这个功能来达到我们的目的。</p>
<p><img src="assets/cc005a70-9b22-11ea-bcff-e5fb1076ab0f" alt="img" /></p>
<p>引入相应 jar 包的支持：</p>
<pre><code class="language-xml">&lt;!--基于 reactive stream 的 redis --&gt;
&lt;dependency&gt;
    &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
    &lt;artifactId&gt;spring-boot-starter-data-redis-reactive&lt;/artifactId&gt;
&lt;/dependency&gt;

</code></pre>
<p>配置基于 IP 进行限流，比如在商场兑换优惠券时，在固定时间内，仅有固定数量的商场优惠券来应对突然间的大量请求，很容易出现高峰交易的情况，导致服务卡死不可用。</p>
<pre><code class="language-yaml">        - name: RequestRateLimiter
          args: 
            redis-rate-limiter.replenishRate: 3 #允许用户每秒处理多少个请求
            redis-rate-limiter.burstCapacity: 5 #令牌桶的容量，允许在一秒钟内完成的最大请求数
            key-resolver: &quot;#{@remoteAddrKeyResolver}&quot; #SPEL 表达式去的对应的 bean

</code></pre>
<p>上文的 KeyResolver 配置项是用来定义按什么规则来限流，比如本次采用 IP 进行限流，编写对应的实现类实现此接口：</p>
<pre><code class="language-java">public class AddrKeyResolver implements KeyResolver {

    @Override
    public Mono&lt;String&gt; resolve(ServerWebExchange exchange) {
        return Mono.just(exchange.getRequest().getRemoteAddress().getAddress().getHostAddress());
    }

}

</code></pre>
<p>在启动类进行 @Bean 定义：</p>
<pre><code class="language-java">    @Bean
    public AddrKeyResolver addrKeyResolver() {
        return new AddrKeyResolver();
    }

</code></pre>
<p>到此，配置完毕，下面来验证配置是否生效。</p>
<h4><strong>测评限流是否生效</strong></h4>
<p>前期我们采用了 PostMan 组件进行了不少接口测试工作，其实它可以提供并发测试功能，不少用过的小伙伴尚未发现这一功能，这里就带大家一起使用 PostMan 来发起并发测试，操作步骤如下。</p>
<p><strong>1. 建立测试脚本目录</strong></p>
<p><img src="assets/126ad2a0-9b24-11ea-9b46-678a499933e3" alt="img" /></p>
<p><strong>2. 将测试请求放入目录</strong></p>
<p><img src="assets/1fed1320-9b24-11ea-a470-713f9388c33a" alt="img" /></p>
<p><strong>3. 运行脚本</strong></p>
<p><img src="assets/3e33ede0-9b24-11ea-84f6-537b473909fa" alt="img" /></p>
<p><img src="assets/4b85cf90-9b24-11ea-8fdb-97e36705b18a" alt="img" /></p>
<p><strong>4. 打开终端</strong>，进入 Redis 对应的库，输入 <code>monitor</code> 命令，监控 Redis 命令的执行情况。点击上图“Run”按钮，查看 Redis 命令的执行情况。查看 Postman 控制台，可以看到有 3 次已经被忽略执行。</p>
<p><img src="assets/67469bb0-9b24-11ea-bcff-e5fb1076ab0f" alt="img" /></p>
<p>到此，通过原生限流组件可以正常使用，通过 IP 是简单的限流，往往还会有更多个性化的需求，这个时候就需要定制来完成高阶功能。</p>
<h3>跨域支持</h3>
<p>时下流行的系统部署架构基本是前、后端独立部署，由此而直接引发另一个问题——跨域请求。必须要在网关层支持跨域，不然无法将请求路由到正确的处理节点。这里提供两种方式，一种是代码编写，一种是能过配置文件配置，建议采用配置方式完成。</p>
<h4><strong>代码方式</strong></h4>
<pre><code class="language-java">@Configuration
public class CORSConfiguration {

    @Bean
    public CorsWebFilter corsWebFilter() {
        CorsConfiguration config = new CorsConfiguration();
        config.setAllowCredentials(Boolean.TRUE);
        //config.addAllowedMethod(&quot;*&quot;);
        config.addAllowedOrigin(&quot;*&quot;);
        config.addAllowedHeader(&quot;*&quot;);
        config.addExposedHeader(&quot;setToken&quot;);

        UrlBasedCorsConfigurationSource source = new UrlBasedCorsConfigurationSource(new PathPatternParser());
        source.registerCorsConfiguration(&quot;/**&quot;, config);

        return new CorsWebFilter(source);
    }
}

</code></pre>
<h4><strong>配置文件配置</strong></h4>
<pre><code class="language-yaml">spring:
  cloud:
    gateway:
      discovery:
      # 跨域
      globalcors:
        corsConfigurations:
          '[/**]':
            allowedHeaders: &quot;*&quot;
            allowedOrigins: &quot;*&quot;
            # 为保证请求的安全，项目中只支持 get 或 post 请求，其它请求全部屏蔽，以免导致多余的问题
            allowedMethods:
            - POST

</code></pre>
<p>本文到此，网关中路由配置、熔断失败、请求限流、请求跨域等常见的共性问题都得到初步的解决，相信随着使用的深入，还有更多高阶的功能等待大家去开发使用。</p>
<p>留一个思考题：</p>
<ul>
<li>除了 Spring Cloud Gateway 之外，你还知道其它中间件可以实现网关功能吗？不妨去调研一番。</li>
</ul>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="14&#32;Spring&#32;Cloud&#32;与&#32;Dubbo&#32;冲突吗——强强联合.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="16&#32;服务压力大系统响应慢如何破——网关流量控制.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434e4c9eed70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/SpringCloud%E5%BE%AE%E6%9C%8D%E5%8A%A1%E5%AE%9E%E6%88%98%EF%BC%88%E5%AE%8C%EF%BC%89/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
