<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>02 WebFlux 快速入门实践.md</title>
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

                    
                    <a href="01&#32;导读：课程概要.md">01 导读：课程概要.md</a>

                </li>
                <li>

                    <a class="current-tab" href="02&#32;WebFlux&#32;快速入门实践.md">02 WebFlux 快速入门实践.md</a>
                    

                </li>
                <li>

                    
                    <a href="03&#32;WebFlux&#32;Web&#32;CRUD&#32;实践.md">03 WebFlux Web CRUD 实践.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;WebFlux&#32;整合&#32;MongoDB.md">04 WebFlux 整合 MongoDB.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;WebFlux&#32;整合&#32;Thymeleaf.md">05 WebFlux 整合 Thymeleaf.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;WebFlux&#32;中&#32;Thymeleaf&#32;和&#32;MongoDB&#32;实践.md">06 WebFlux 中 Thymeleaf 和 MongoDB 实践.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;WebFlux&#32;整合&#32;Redis.md">07 WebFlux 整合 Redis.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;WebFlux&#32;中&#32;Redis&#32;实现缓存.md">08 WebFlux 中 Redis 实现缓存.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;WebFlux&#32;中&#32;WebSocket&#32;实现通信.md">09 WebFlux 中 WebSocket 实现通信.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;WebFlux&#32;集成测试及部署.md">10 WebFlux 集成测试及部署.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;WebFlux&#32;实战图书管理系统.md">11 WebFlux 实战图书管理系统.md</a>

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
                        <div><h1>02 WebFlux 快速入门实践</h1>
<h3>Spring Boot 2.0</h3>
<p>spring.io 官网有句醒目的话是：</p>
<pre><code>BUILD ANYTHING WITH SPRING BOOT

</code></pre>
<p>Spring Boot （Boot 顾名思义，是引导的意思）框架是用于简化 Spring 应用从搭建到开发的过程。应用开箱即用，只要通过一个指令，包括命令行 <code>java -jar</code> 、<code>SpringApplication</code> 应用启动类 、 Spring Boot Maven 插件等，就可以启动应用了。另外，Spring Boot 强调只需要很少的配置文件，所以在开发生产级 Spring 应用中，让开发变得更加高效和简易。目前，Spring Boot 版本是 2.x 版本。Spring Boot 包括 WebFlux。</p>
<p><img src="assets/87db53c0-b936-11e7-b969-cb3cfaf54002-1608971096373" alt="img" /></p>
<h3>Spring Boot 2.0 WebFlux</h3>
<p>了解 WebFlux，首先了解下什么是 Reactive Streams。Reactive Streams 是 JVM 中面向流的库标准和规范：</p>
<ul>
<li>处理可能无限数量的元素</li>
<li>按顺序处理</li>
<li>组件之间异步传递</li>
<li>强制性非阻塞背压（Backpressure）</li>
</ul>
<p><strong>Backpressure（背压）</strong></p>
<p>背压是一种常用策略，使得发布者拥有无限制的缓冲区存储元素，用于确保发布者发布元素太快时，不会去压制订阅者。</p>
<p><strong>Reactive Streams（响应式流）</strong></p>
<p>一般由以下组成：</p>
<ul>
<li>发布者：发布元素到订阅者</li>
<li>订阅者：消费元素</li>
<li>订阅：在发布者中，订阅被创建时，将与订阅者共享</li>
<li>处理器：发布者与订阅者之间处理数据</li>
</ul>
<p><strong>响应式编程</strong></p>
<p>有了 Reactive Streams 这种标准和规范，利用规范可以进行响应式编程。那再了解下什么是 Reactive programming 响应式编程。响应式编程是基于异步和事件驱动的非阻塞程序，只是垂直通过在 JVM 内启动少量线程扩展，而不是水平通过集群扩展。这就是一个编程范例，具体项目中如何体现呢？</p>
<p>响应式项目编程实战中，通过基于 Reactive Streams 规范实现的框架 Reactor 去实战。Reactor 一般提供两种响应式 API ：</p>
<ul>
<li>Mono：实现发布者，并返回 0 或 1 个元素</li>
<li>Flux：实现发布者，并返回 N 个元素</li>
</ul>
<p><strong>Spring Webflux</strong></p>
<p>Spring Boot Webflux 就是基于 Reactor 实现的。Spring Boot 2.0 包括一个新的 spring-webflux 模块。该模块包含对响应式 HTTP 和 WebSocket 客户端的支持，以及对 REST，HTML 和 WebSocket 交互等程序的支持。一般来说，Spring MVC 用于同步处理，Spring Webflux 用于异步处理。</p>
<p>Spring Boot Webflux 有两种编程模型实现，一种类似 Spring MVC 注解方式，另一种是使用其功能性端点方式。注解的会在第二篇文章讲到，下面快速入门用 Spring Webflux 功能性方式实现。</p>
<h3>Spring Boot 2.0 WebFlux 特性</h3>
<p>常用的 Spring Boot 2.0 WebFlux 生产的特性如下：</p>
<ul>
<li>响应式 API</li>
<li>编程模型</li>
<li>适用性</li>
<li>内嵌容器</li>
<li>Starter 组件</li>
</ul>
<p>还有对日志、Web、消息、测试及扩展等支持。</p>
<h4>响应式 API</h4>
<p>Reactor 框架是 Spring Boot Webflux 响应库依赖，通过 Reactive Streams 并与其他响应库交互。提供了 两种响应式 API：Mono 和 Flux。一般是将 Publisher 作为输入，在框架内部转换成 Reactor 类型并处理逻辑，然后返回 Flux 或 Mono 作为输出。</p>
<h4>适用性</h4>
<p><img src="assets/e39654d047bd43a8f708d67f947c00c01523267.png" alt="file" /></p>
<p>一图就很明确了，WebFlux 和 MVC 有交集，方便大家迁移。但是注意：</p>
<ul>
<li>MVC 能满足场景的，就不需要更改为 WebFlux。</li>
<li>要注意容器的支持，可以看看下面内嵌容器的支持。</li>
<li>微服务体系结构，WebFlux 和 MVC 可以混合使用。尤其开发 IO 密集型服务的时候，选择 WebFlux 去实现。</li>
</ul>
<h4>编程模型</h4>
<p>Spring 5 web 模块包含了 Spring WebFlux 的 HTTP 抽象。类似 Servlet API , WebFlux 提供了 WebHandler API 去定义非阻塞 API 抽象接口。可以选择以下两种编程模型实现：</p>
<ul>
<li>注解控制层。和 MVC 保持一致，WebFlux 也支持响应性 @RequestBody 注解。</li>
<li>功能性端点。基于 lambda 轻量级编程模型，用来路由和处理请求的小工具。和上面最大的区别就是，这种模型，全程控制了请求 - 响应的生命流程</li>
</ul>
<h4>内嵌容器</h4>
<p>跟 Spring Boot 大框架一样启动应用，但 WebFlux 默认是通过 Netty 启动，并且自动设置了默认端口为 8080。另外还提供了对 Jetty、Undertow 等容器的支持。开发者自行在添加对应的容器 Starter 组件依赖，即可配置并使用对应内嵌容器实例。</p>
<p>但是要注意，必须是 Servlet 3.1+ 容器，如 Tomcat、Jetty；或者非 Servlet 容器，如 Netty 和 Undertow。</p>
<h4>Starter 组件</h4>
<p>跟 Spring Boot 大框架一样，Spring Boot Webflux 提供了很多 “开箱即用” 的 Starter 组件。Starter 组件是可被加载在应用中的 Maven 依赖项。只需要在 Maven 配置中添加对应的依赖配置，即可使用对应的 Starter 组件。例如，添加 <code>spring-boot-starter-webflux</code> 依赖，就可用于构建响应式 API 服务，其包含了 Web Flux 和 Tomcat 内嵌容器等。</p>
<p>开发中，很多功能是通过添加 Starter 组件的方式来进行实现。那么，Spring Boot 2.x 常用的 Starter 组件有哪些呢？</p>
<h3>Spring Boot 2.0 WebFlux 组件</h3>
<p>Spring Boot WebFlux 官方提供了很多 Starter 组件，每个模块会有多种技术实现选型支持，来实现各种复杂的业务需求：</p>
<ul>
<li>Web：Spring WebFlux</li>
<li>模板引擎：Thymeleaf</li>
<li>存储：Redis、MongoDB、Cassandra，不支持 MySQL</li>
<li>内嵌容器：Tomcat、Jetty、Undertow</li>
</ul>
<h3>Spring Initializr 快速构建项目骨架</h3>
<p>Spring Boot Maven 工程，就是普通的 Maven 工程，加入了对应的 Spring Boot 依赖即可。Spring Initializr 则是像代码生成器一样，自动就给你出来了一个 Spring Boot Maven 工程。Spring Initializr 有两种方式可以得到 Spring Boot Maven 骨架工程：</p>
<h4>start.spring.io 在线生成</h4>
<p>Spring 官方提供了名为 Spring Initializr 的网站，去引导你快速生成 Spring Boot 应用。网站地址，<a href="https://start.spring.io/">详见这里</a>，操作步骤如下：</p>
<p>第一步，选择 Maven 或者 Gradle 构建工具，开发语言 Java 、Kotlin 或者 Groovy，最后确定 Spring Boot 版本号。这里默认选择 Maven 构建工具、Java 开发语言和 Spring Boot 2.0.1。</p>
<p>第二步，输入 Maven 工程信息，即项目组 groupId 和名字 artifactId，这里对应 Maven 信息为：</p>
<ul>
<li>groupId：springboot</li>
<li>artifactId：sspringboot-webflux-1-quickstart</li>
</ul>
<p>这里默认版本号 version 为 0.0.1-SNAPSHOT，三个属性在 Maven 依赖仓库是唯一标识的。</p>
<p>第三步，选择工程需要的 Starter 组件和其他依赖，最后单击“生成”按钮，即可获得骨架工程压缩包，这里快速入门，只要选择 Reactive Web 即可，如图所示。</p>
<p><img src="assets/e8756dce7ada604d9f29f2fd61d0f1721523318.png" alt="img" /></p>
<h3>配置 POM 依赖</h3>
<p>检查工程 POM 文件中，是否配置了 spring-boot-starter-webflux 依赖。如果是上面自动生成的，配置如下：</p>
<pre><code>  &lt;dependencies&gt;
    &lt;dependency&gt;
      &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
      &lt;artifactId&gt;spring-boot-starter-webflux&lt;/artifactId&gt;
    &lt;/dependency&gt;

    &lt;dependency&gt;
      &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
      &lt;artifactId&gt;spring-boot-starter-test&lt;/artifactId&gt;
      &lt;scope&gt;test&lt;/scope&gt;
    &lt;/dependency&gt;
    &lt;dependency&gt;
      &lt;groupId&gt;io.projectreactor&lt;/groupId&gt;
      &lt;artifactId&gt;reactor-test&lt;/artifactId&gt;
      &lt;scope&gt;test&lt;/scope&gt;
    &lt;/dependency&gt;
  &lt;/dependencies&gt;

  &lt;build&gt;
    &lt;plugins&gt;
      &lt;plugin&gt;
        &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
        &lt;artifactId&gt;spring-boot-maven-plugin&lt;/artifactId&gt;
      &lt;/plugin&gt;
    &lt;/plugins&gt;
  &lt;/build&gt;

</code></pre>
<p>spring-boot-starter-webflux 依赖，是我们核心需要学习 webflux 的包，里面默认包含了 spring-boot-starter-reactor-netty 、spring 5 webflux 包，也就是说默认是通过 netty 启动的。</p>
<p>reactor-test、spring-boot-starter-test 两个依赖搭配是用于单元测试。</p>
<p>spring-boot-maven-plugin 是 Spring Boot Maven 插件，可以运行、编译等调用。</p>
<h3>编写处理器类 Handler</h3>
<p>新建包 org.spring.springboot.handler，作为编写功能处理类。新建城市（City）例子的处理类 CityHandler，代码如下：</p>
<pre><code>import org.springframework.http.MediaType;
import org.springframework.stereotype.Component;
import org.springframework.web.reactive.function.BodyInserters;
import org.springframework.web.reactive.function.server.ServerRequest;
import org.springframework.web.reactive.function.server.ServerResponse;
import reactor.core.publisher.Mono;

@Component
public class CityHandler {

    public Mono&lt;ServerResponse&gt; helloCity(ServerRequest request) {
        return ServerResponse.ok().contentType(MediaType.TEXT_PLAIN)
                .body(BodyInserters.fromObject(&quot;Hello, City!&quot;));
    }
}

</code></pre>
<p>ServerResponse 是对响应的封装，可以设置响应状态、响应头、响应正文。比如 ok 代表的是 200 响应码、MediaType 枚举是代表这文本内容类型、返回的是 String 的对象。</p>
<p>这里用 Mono 作为返回对象，是因为返回包含了一个 ServerResponse 对象，而不是多个元素。</p>
<h3>编写路由器类 Router</h3>
<p>新建 org.spring.springboot.router 包，作为编写路由器类。新建城市（City）例子的路由类 CityRouter，代码如下：</p>
<pre><code>import org.spring.springboot.handler.CityHandler;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.http.MediaType;
import org.springframework.web.reactive.function.server.RequestPredicates;
import org.springframework.web.reactive.function.server.RouterFunction;
import org.springframework.web.reactive.function.server.RouterFunctions;
import org.springframework.web.reactive.function.server.ServerResponse;

@Configuration
public class CityRouter {

    @Bean
    public RouterFunction&lt;ServerResponse&gt; routeCity(CityHandler cityHandler) {
        return RouterFunctions
                .route(RequestPredicates.GET(&quot;/hello&quot;)
                                .and(RequestPredicates.accept(MediaType.TEXT_PLAIN)),
                        cityHandler::helloCity);
    }

}

</code></pre>
<p>RouterFunctions 对请求路由处理类，即将请求路由到处理器，这里将一个 GET 请求 /hello 路由到处理器 cityHandler 的 helloCity 方法上。跟 Spring MVC 模式下的 HandleMapping 的作用类似。</p>
<p>RouterFunctions.route(RequestPredicate, HandlerFunction) 方法，对应的入参是请求参数和处理函数，如果请求匹配，就调用对应的处理器函数。</p>
<p>到这里一个简单的服务就写好了，下面怎么运行该服务。</p>
<h3>启动运行项目</h3>
<p>一个简单的 Spring Boot Webflux 工程就开发完毕了，下面运行工程验证下。使用 IDEA 右侧工具栏，点击 Maven Project Tab ，点击使用下 Maven 插件的 install 命令，或者使用命令行的形式，在工程根目录下，执行 Maven 清理和安装工程的指令：</p>
<pre><code>cd springboot-webflux-1-quickstart
mvn clean install

</code></pre>
<p>在控制台中看到成功的输出：</p>
<pre><code>... 省略
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time: 01:30 min
[INFO] Finished at: 2017-10-15T10:00:54+08:00
[INFO] Final Memory: 31M/174M
[INFO] ------------------------------------------------------------------------

</code></pre>
<h4>运行工程</h4>
<p>在 IDEA 中执行 Application 类启动，任意正常模式或者 Debug 模式，可以在控制台看到成功运行的输出：</p>
<pre><code>... 省略
2018-04-10 08:43:39.932  INFO 2052 --- [ctor-http-nio-1] r.ipc.netty.tcp.BlockingNettyContext     : Started HttpServer on /0:0:0:0:0:0:0:0:8080
2018-04-10 08:43:39.935  INFO 2052 --- [           main] o.s.b.web.embedded.netty.NettyWebServer  : Netty started on port(s): 8080
2018-04-10 08:43:39.960  INFO 2052 --- [           main] org.spring.springboot.Application        : Started Application in 6.547 seconds (JVM running for 9.851)

</code></pre>
<p>一看，确实是 Netty 启动的。</p>
<p>打开浏览器，访问 /hello 地址，会看到如图所示的返回结果：</p>
<p><img src="assets/42a9f1eaa1ee54923556727eac2216481523320.png" alt="file" /></p>
<h3>总结</h3>
<p>本文主要讲了 Spring Boot 2.0 WebFlux 背景和快速入门使用，用的是基于功能性端点去创建一个服务，但这个有点代码偏多。下一课一个 CRUD 我们使用注解控制层，让开发更方便。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="01&#32;导读：课程概要.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="03&#32;WebFlux&#32;Web&#32;CRUD&#32;实践.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4355c69d5d645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/%E6%A1%88%E4%BE%8B%E4%B8%8A%E6%89%8B%20Spring%20Boot%20WebFlux%EF%BC%88%E5%AE%8C%EF%BC%89/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
