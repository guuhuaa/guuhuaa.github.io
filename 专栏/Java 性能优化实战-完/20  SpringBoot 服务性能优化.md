<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>20  SpringBoot 服务性能优化.md</title>
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

                    
                    <a href="00&#32;Java&#32;性能优化，是进阶高级架构师的炼金石.md">00 Java 性能优化，是进阶高级架构师的炼金石.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;理论分析：性能优化，有哪些衡量指标？需要注意什么？.md">01 理论分析：性能优化，有哪些衡量指标？需要注意什么？.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;理论分析：性能优化有章可循，谈谈常用的切入点.md">02 理论分析：性能优化有章可循，谈谈常用的切入点.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;深入剖析：哪些资源，容易成为瓶颈？.md">03 深入剖析：哪些资源，容易成为瓶颈？.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;工具实践：如何获取代码性能数据？.md">04 工具实践：如何获取代码性能数据？.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;工具实践：基准测试&#32;JMH，精确测量方法性能.md">05 工具实践：基准测试 JMH，精确测量方法性能.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;案例分析：缓冲区如何让代码加速.md">06 案例分析：缓冲区如何让代码加速.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;&#32;案例分析：无处不在的缓存，高并发系统的法宝.md">07  案例分析：无处不在的缓存，高并发系统的法宝.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;&#32;案例分析：Redis&#32;如何助力秒杀业务.md">08  案例分析：Redis 如何助力秒杀业务.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;&#32;案例分析：池化对象的应用场景.md">09  案例分析：池化对象的应用场景.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;&#32;案例分析：大对象复用的目标和注意点.md">10  案例分析：大对象复用的目标和注意点.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;&#32;案例分析：如何用设计模式优化性能.md">11  案例分析：如何用设计模式优化性能.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;&#32;案例分析：并行计算让代码“飞”起来.md">12  案例分析：并行计算让代码“飞”起来.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;&#32;案例分析：多线程锁的优化.md">13  案例分析：多线程锁的优化.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;&#32;案例分析：乐观锁和无锁.md">14  案例分析：乐观锁和无锁.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;&#32;案例分析：从&#32;BIO&#32;到&#32;NIO，再到&#32;AIO.md">15  案例分析：从 BIO 到 NIO，再到 AIO.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;&#32;案例分析：常见&#32;Java&#32;代码优化法则.md">16  案例分析：常见 Java 代码优化法则.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;&#32;高级进阶：JVM&#32;如何完成垃圾回收？.md">17  高级进阶：JVM 如何完成垃圾回收？.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;&#32;高级进阶：JIT&#32;如何影响&#32;JVM&#32;的性能？.md">18  高级进阶：JIT 如何影响 JVM 的性能？.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;&#32;高级进阶：JVM&#32;常见优化参数.md">19  高级进阶：JVM 常见优化参数.md</a>

                </li>
                <li>

                    <a class="current-tab" href="20&#32;&#32;SpringBoot&#32;服务性能优化.md">20  SpringBoot 服务性能优化.md</a>
                    

                </li>
                <li>

                    
                    <a href="21&#32;&#32;性能优化的过程方法与求职面经总结.md">21  性能优化的过程方法与求职面经总结.md</a>

                </li>
                <li>

                    
                    <a href="22&#32;结束语&#32;&#32;实践出真知.md">22 结束语  实践出真知.md</a>

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
                        <div><h1>20  SpringBoot 服务性能优化</h1>
<p>在开始对 SpringBoot 服务进行性能优化之前，你需要做一些准备，把 SpringBoot 服务的一些数据暴露出来。比如，你的服务用到了缓存，就需要把缓存命中率这些数据进行收集；用到了数据库连接池，就需要把连接池的参数给暴露出来。</p>
<p>我们这里采用的监控工具是 Prometheus，它是一个是时序数据库，能够存储我们的指标。SpringBoot 可以非常方便地接入到 Prometheus 中。</p>
<h3>SpringBoot 如何开启监控？</h3>
<p>创建一个 SpringBoot 项目后，首先加入 maven 依赖。</p>
<pre><code>&lt;dependency&gt;
     &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
     &lt;artifactId&gt;spring-boot-starter-actuator&lt;/artifactId&gt;
 &lt;/dependency&gt;
 &lt;dependency&gt;
     &lt;groupId&gt;io.micrometer&lt;/groupId&gt;
     &lt;artifactId&gt;micrometer-registry-prometheus&lt;/artifactId&gt;
 &lt;/dependency&gt;
 &lt;dependency&gt;
     &lt;groupId&gt;io.micrometer&lt;/groupId&gt;
     &lt;artifactId&gt;micrometer-core&lt;/artifactId&gt;
 &lt;/dependency&gt;
</code></pre>
<p>然后，我们需要在 application.properties 配置文件中，开放相关的监控接口。</p>
<pre><code>management.endpoint.metrics.enabled=true
management.endpoints.web.exposure.include=*
management.endpoint.prometheus.enabled=true
management.metrics.export.prometheus.enabled=true
</code></pre>
<p>启动之后，我们就可以通过访问<a href="http://localhost:8080/actuator/prometheus">监控接口</a>来获取监控数据。</p>
<p><img src="assets/CgqCHl9htcuAAw51AAK0O_g_pbM862.png" alt="Drawing 0.png" /></p>
<p>想要监控业务数据也是比较简单的，你只需要注入一个 MeterRegistry 实例即可，下面是一段示例代码：</p>
<pre><code>@Autowired
MeterRegistry registry;

@GetMapping(&quot;/test&quot;)
@ResponseBody
public String test() {
    registry.counter(&quot;test&quot;,
            &quot;from&quot;, &quot;127.0.0.1&quot;,
            &quot;method&quot;, &quot;test&quot;
    ).increment();

    return &quot;ok&quot;;
}
</code></pre>
<p>从监控连接中，我们可以找到刚刚添加的监控信息。</p>
<pre><code>test_total{from=&quot;127.0.0.1&quot;,method=&quot;test&quot;,} 5.0
</code></pre>
<p>这里简单介绍一下流行的<strong>Prometheus 监控体系</strong>，Prometheus 使用拉的方式获取监控数据，这个暴露数据的过程可以交给功能更加齐全的 telegraf 组件。</p>
<p><img src="assets/CgqCHl9htdiAO89HAAK1NRYCNZE604.png" alt="Drawing 1.png" /></p>
<p>如上图，我们通常使用 Grafana 进行监控数据的展示，使用 AlertManager 组件进行提前预警。这一部分的搭建工作不是我们的重点，感兴趣的同学可自行研究。</p>
<p>下图便是一张典型的监控图，可以看到 Redis 的缓存命中率等情况。</p>
<p><img src="assets/Ciqc1F9htd-AXIKHAANYYdIDl6g753.png" alt="Drawing 2.png" /></p>
<h3>Java 生成火焰图</h3>
<p><strong>火焰图</strong>是用来分析程序运行瓶颈的工具。</p>
<p>火焰图也可以用来分析 Java 应用。可以从 <a href="https://github.com/jvm-profiling-tools/async-profiler">github</a> 上下载 async-profiler 的压缩包进行相关操作。比如，我们把它解压到 /root/ 目录，然后以 javaagent 的方式来启动 Java 应用，命令行如下：</p>
<pre><code>java -agentpath:/root/build/libasyncProfiler.so=start,svg,file=profile.svg -jar spring-petclinic-2.3.1.BUILD-SNAPSHOT.jar
</code></pre>
<p>运行一段时间后，停止进程，可以看到在当前目录下，生成了 profile.svg 文件，这个文件是可以用浏览器打开的。
如下图所示，纵向，表示的是调用栈的深度；横向，表明的是消耗的时间。所以格子的宽度越大，越说明它可能是一个瓶颈。一层层向下浏览，即可找到需要优化的目标。</p>
<p><img src="assets/Ciqc1F9htfOAN3G1AEK7W4TM0AU264.gif" alt="2020-08-21 17-07-35.2020-08-21 17_12_29.gif" /></p>
<h3>优化思路</h3>
<p>对一个普通的 Web 服务来说，我们来看一下，要访问到具体的数据，都要经历哪些主要的环节？</p>
<p>如下图，在浏览器中输入相应的域名，需要通过 DNS 解析到具体的 IP 地址上，为了保证高可用，我们的服务一般都会部署多份，然后使用 Nginx 做反向代理和负载均衡。</p>
<p><img src="assets/Ciqc1F9htgCAcdwGAAIVQmXnOPo885.png" alt="Drawing 4.png" /></p>
<p>Nginx 根据资源的特性，会承担一部分动静分离的功能。其中，动态功能部分，会进入我们的SpringBoot 服务。</p>
<p>SpringBoot 默认使用内嵌的 tomcat 作为 Web 容器，使用典型的 MVC 模式，最终访问到我们的数据。</p>
<h3>HTTP 优化</h3>
<p>下面我们举例来看一下，哪些动作能够加快网页的获取。为了描述方便，我们仅讨论 HTTP1.1 协议的。</p>
<p><strong>1.使用 CDN 加速文件获取</strong></p>
<p>比较大的文件，尽量使用 CDN（Content Delivery Network）分发，甚至是一些常用的前端脚本、样式、图片等，都可以放到 CDN 上。CDN 通常能够加快这些文件的获取，网页加载也更加迅速。</p>
<p><strong>2.合理设置 Cache-Control 值</strong></p>
<p>浏览器会判断 HTTP 头 Cache-Control 的内容，用来决定是否使用浏览器缓存，这在管理一些静态文件的时候，非常有用，相同作用的头信息还有 Expires。Cache-Control 表示多久之后过期；Expires 则表示什么时候过期。</p>
<p>这个参数可以在 Nginx 的配置文件中进行设置。</p>
<pre><code>location ~* ^.+\.(ico|gif|jpg|jpeg|png)$ { 
            # 缓存1年
            add_header Cache-Control: no-cache, max-age=31536000;
}
</code></pre>
<p><strong>3.减少单页面请求域名的数量</strong></p>
<p>减少每个页面请求的域名数量，尽量保证在 4 个之内。这是因为，浏览器每次访问后端的资源，都需要先查询一次 DNS，然后找到 DNS 对应的 IP 地址，再进行真正的调用。</p>
<p>DNS 有多层缓存，比如浏览器会缓存一份、本地主机会缓存、ISP 服务商缓存等。从 DNS 到 IP 地址的转变，通常会花费 20-120ms 的时间。减少域名的数量，可加快资源的获取。</p>
<p><strong>4.开启 gzip</strong></p>
<p>开启 gzip，可以先把内容压缩后，浏览器再进行解压。由于减少了传输的大小，会减少带宽的使用，提高传输效率。</p>
<p>在 nginx 中可以很容易地开启，配置如下：</p>
<pre><code>gzip on;
gzip_min_length 1k;
gzip_buffers 4 16k;
gzip_comp_level 6;
gzip_http_version 1.1;
gzip_types text/plain application/javascript text/css;
</code></pre>
<p><strong>5.对资源进行压缩</strong></p>
<p>对 JavaScript 和 CSS，甚至是 HTML 进行压缩。道理类似，现在流行的前后端分离模式，一般都是对这些资源进行压缩的。</p>
<p><strong>6.使用 keepalive</strong></p>
<p>由于连接的创建和关闭，都需要耗费资源。用户访问我们的服务后，后续也会有更多的互动，所以保持长连接可以显著减少网络交互，提高性能。</p>
<p>nginx 默认开启了对客户端的 keep avlide 支持，你可以通过下面两个参数来调整它的行为。</p>
<pre><code>http {
    keepalive_timeout  120s 120s;
    keepalive_requests 10000;
}
</code></pre>
<p>nginx 与后端 upstream 的长连接，需要手工开启，参考配置如下：</p>
<pre><code>location ~ /{ 
       proxy_pass http://backend;
       proxy_http_version 1.1;
       proxy_set_header Connection &quot;&quot;;
}
</code></pre>
<h3>自定义 Web 容器</h3>
<p>如果你的项目并发量比较高，想要修改最大线程数、最大连接数等配置信息，可以通过自定义Web 容器的方式，代码如下所示。</p>
<pre><code>@SpringBootApplication(proxyBeanMethods = false)
public class App implements WebServerFactoryCustomizer&lt;ConfigurableServletWebServerFactory&gt; {
    public static void main(String[] args) {
        SpringApplication.run(PetClinicApplication.class, args);
    }
    @Override
    public void customize(ConfigurableServletWebServerFactory factory) {
        TomcatServletWebServerFactory f = (TomcatServletWebServerFactory) factory;
        f.setProtocol(&quot;org.apache.coyote.http11.Http11Nio2Protocol&quot;);

        f.addConnectorCustomizers(c -&gt; {
            Http11NioProtocol protocol = (Http11NioProtocol) c.getProtocolHandler();
            protocol.setMaxConnections(200);
            protocol.setMaxThreads(200);
            protocol.setSelectorTimeout(3000);
            protocol.setSessionTimeout(3000);
            protocol.setConnectionTimeout(3000);
        });
    }
}
</code></pre>
<p>注意上面的代码，我们设置了它的协议为 org.apache.coyote.http11.Http11Nio2Protocol，意思就是开启了 Nio2。这个参数在 Tomcat 8.0之后才有，开启之后会增加一部分性能。
对比如下（测试项目代码见 <a href="https://gitee.com/xjjdog/tuning-lagou-res/tree/master/tuning-020/spring-petclinic-main">spring-petclinic-main</a>）：</p>
<p>默认。</p>
<pre><code>[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="7e0c11110a3e12111d1f1216110d0a">[email&#160;protected]</a> wrk2-master]# ./wrk -t2 -c100 -d30s -R2000 http://172.16.1.57:8080/owners?lastName=
Running 30s test @ http://172.16.1.57:8080/owners?lastName=
  2 threads and 100 connections
  Thread calibration: mean lat.: 4588.131ms, rate sampling interval: 16277ms
  Thread calibration: mean lat.: 4647.927ms, rate sampling interval: 16285ms
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    16.49s     4.98s   27.34s    63.90%
    Req/Sec   106.50      1.50   108.00    100.00%
  6471 requests in 30.03s, 39.31MB read
  Socket errors: connect 0, read 0, write 0, timeout 60
Requests/sec:    215.51
Transfer/sec:      1.31MB
</code></pre>
<p>Nio2。</p>
<pre><code>[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="cebca1a1ba8ea2a1adafa2a6a1bdba">[email&#160;protected]</a> wrk2-master]# ./wrk -t2 -c100 -d30s -R2000 http://172.16.1.57:8080/owners?lastName=
Running 30s test @ http://172.16.1.57:8080/owners?lastName=
  2 threads and 100 connections
  Thread calibration: mean lat.: 4358.805ms, rate sampling interval: 15835ms
  Thread calibration: mean lat.: 4622.087ms, rate sampling interval: 16293ms
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    17.47s     4.98s   26.90s    57.69%
    Req/Sec   125.50      2.50   128.00    100.00%
  7469 requests in 30.04s, 45.38MB read
  Socket errors: connect 0, read 0, write 0, timeout 4
Requests/sec:    248.64
Transfer/sec:      1.51MB
</code></pre>
<p>你甚至可以将 tomcat 替换成 undertow。undertow 也是一个 Web 容器，更加轻量级一些，占用的内存更少，启动的守护进程也更少，更改方式如下：</p>
<pre><code>&lt;dependency&gt;
      &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
      &lt;artifactId&gt;spring-boot-starter-web&lt;/artifactId&gt;
      &lt;exclusions&gt;
        &lt;exclusion&gt;
          &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
          &lt;artifactId&gt;spring-boot-starter-tomcat&lt;/artifactId&gt;
        &lt;/exclusion&gt;
      &lt;/exclusions&gt;
    &lt;/dependency&gt;
    &lt;dependency&gt;
      &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
      &lt;artifactId&gt;spring-boot-starter-undertow&lt;/artifactId&gt;
    &lt;/dependency&gt;
</code></pre>
<p>其实，对于 tomcat 优化最为有效的，还是 JVM 参数的配置，你可以参考上一课时的内容进行调整。
比如，使用下面的参数启动，QPS 由 248 上升到 308。</p>
<pre><code>-XX:+UseG1GC -Xmx2048m -Xms2048m -XX:+AlwaysPreTouch
</code></pre>
<h3>Skywalking</h3>
<p>对于一个 web 服务来说，最缓慢的地方就在于数据库操作。所以，使用“07 | 案例分析：无处不在的缓存，高并发系统的法宝”和“08 | 案例分析：Redis 如何助力秒杀业务”提供的本地缓存和分布式缓存优化，能够获得最大的性能提升。</p>
<p>对于如何定位到复杂分布式环境中的问题，我这里想要分享另外一个工具：Skywalking。</p>
<p>Skywalking 是使用探针技术（JavaAgent）来实现的。通过在 Java 的启动参数中，加入 javaagent 的 Jar 包，即可将性能数据和调用链数据封装，并发送到 Skywalking 的服务器。</p>
<p>下载相应的安装包（如果使用 ES 存储，需要下载专用的安装包），配置好存储之后，即可一键启动。</p>
<p>将 agent 的压缩包，解压到相应的目录。</p>
<pre><code>tar xvf skywalking-agent.tar.gz  -C /opt/
</code></pre>
<p>在业务启动参数中加入 agent 的包。比如，原来的启动命令是：</p>
<pre><code>java  -jar /opt/test-service/spring-boot-demo.jar  --spring.profiles.active=dev
</code></pre>
<p>改造后的启动命令是：</p>
<pre><code>java -javaagent:/opt/skywalking-agent/skywalking-agent.jar -Dskywalking.agent.service_name=the-demo-name  -jar /opt/test-service/spring-boot-demo.ja  --spring.profiles.active=dev
</code></pre>
<p>访问一些服务的链接，打开 Skywalking 的 UI，即可看到下图的界面。这些指标可以类比“01 | 理论分析：性能优化，有哪些衡量指标？需要注意什么？”提到的衡量指标去理解，我们就可以从图中找到响应比较慢 QPS 又比较高的接口，进行专项优化。</p>
<p><img src="assets/Ciqc1F9htwyARKqMAAgxG3QYe8A553.png" alt="Drawing 5.png" /></p>
<h3>各个层次的优化方向</h3>
<h4>1.Controller 层</h4>
<p>controller 层用于接收前端的查询参数，然后构造查询结果。现在很多项目都采用前后端分离的架构，所以 controller 层的方法，一般会使用 @ResponseBody 注解，把查询的结果，解析成 JSON 数据返回（兼顾效率和可读性）。</p>
<p>由于 controller 只是充当了一个类似功能组合和路由的角色，所以这部分对性能的影响就主要体现在数据集的大小上。如果结果集合非常大，JSON 解析组件就要花费较多的时间进行解析，</p>
<p>大结果集不仅会影响解析时间，还会造成内存浪费。</p>
<p>假如结果集在解析成 JSON 之前，占用的内存是 10MB，那么在解析过程中，有可能会使用 20M 或者更多的内存去做这个工作。</p>
<p>我见过很多案例，由于返回对象的嵌套层次太深、引用了不该引用的对象（比如非常大的 byte[] 对象），造成了内存使用的飙升。</p>
<p>所以，<strong>对于一般的服务，保持结果集的精简，是非常有必要的</strong>，这也是 DTO（data transfer object）存在的必要。如果你的项目，返回的结果结构比较复杂，对结果集进行一次转换是非常有必要的。</p>
<h4>2.Service 层</h4>
<p>service 层用于处理具体的业务，大部分功能需求都是在这里完成的。service 层一般是使用单例模式（prototype），很少会保存状态，而且可以被 controller 复用。</p>
<p>service 层的代码组织，对代码的可读性、性能影响都比较大。我们常说的设计模式，大多数都是针对 service 层来说的。</p>
<p>service 层会频繁使用更底层的资源，通过组合的方式获取我们所需要的数据，大多数可以通过我们前面课时提供的优化思路进行优化。</p>
<p>这里要着重提到的一点，就是分布式事务。</p>
<p><img src="assets/CgqCHl9htvaAf1S-AAKlZCq3SXg275.png" alt="Drawing 6.png" /></p>
<p>如上图，四个操作分散在三个不同的资源中。要想达到一致性，需要三个不同的资源 MySQL、MQ、ElasticSearch 进行统一协调。它们底层的协议，以及实现方式，都是不一样的，那就无法通过 Spring 提供的 Transaction 注解来解决，需要借助外部的组件来完成。</p>
<p>很多人都体验过，加入了一些保证一致性的代码，一压测，性能掉的惊掉下巴。分布式事务是性能杀手，因为它要使用额外的步骤去保证一致性，常用的方法有：两阶段提交方案、TCC、本地消息表、MQ 事务消息、分布式事务中间件等。</p>
<p><img src="assets/Ciqc1F9htx6ADeh6AAFoqvxy4eM753.png" alt="Drawing 7.png" /></p>
<p>如上图，分布式事务要在改造成本、性能、时效等方面进行综合考虑。有一个介于分布式事务和非事务之间的名词，叫作<strong>柔性事务</strong>。柔性事务的理念是将业务逻辑和互斥操作，从资源层上移至业务层面。</p>
<p><strong>关于传统事务和柔性事务，我们来简单比较一下。</strong></p>
<p><strong>ACID</strong></p>
<p>关系数据库, 最大的特点就是事务处理, 即满足 ACID。</p>
<ul>
<li>原子性（Atomicity）：事务中的操作要么都做，要么都不做。</li>
<li>一致性（Consistency）：系统必须始终处在强一致状态下。</li>
<li>隔离性（Isolation）：一个事务的执行不能被其他事务所干扰。</li>
<li>持久性（Durability）：一个已提交的事务对数据库中数据的改变是永久性的。</li>
</ul>
<p><strong>BASE</strong></p>
<p>BASE 方法通过牺牲一致性和孤立性来提高可用性和系统性能。</p>
<p>BASE 为 Basically Available、Soft-state、Eventually consistent 三者的缩写，其中 BASE 分别代表：</p>
<ul>
<li>基本可用（Basically Available）：系统能够基本运行、一直提供服务。</li>
<li>软状态（Soft-state）：系统不要求一直保持强一致状态。</li>
<li>最终一致性（Eventual consistency）：系统需要在某一时刻后达到一致性要求。</li>
</ul>
<p>互联网业务，推荐使用补偿事务，完成最终一致性。比如，通过一系列的定时任务，完成对数据的修复。</p>
<h4>3.Dao 层</h4>
<p>经过合理的数据缓存，我们都会尽量避免请求穿透到 Dao 层。除非你对 ORM 本身提供的缓存特性特别的熟悉；否则，都推荐你使用更加通用的方式去缓存数据。</p>
<p>Dao 层，主要在于对 ORM 框架的使用上。比如，在 JPA 中，如果加了一对多或者多对多的映射关系，而又没有开启懒加载，级联查询的时候就容易造成深层次的检索，造成了内存开销大、执行缓慢的后果。</p>
<p>在一些数据量比较大的业务中，多采用分库分表的方式。在这些分库分表组件中，很多简单的查询语句，都会被重新解析后分散到各个节点进行运算，最后进行结果合并。</p>
<p>举个例子，select count(*) from a 这句简单的 count 语句，就可能将请求路由到十几张表中去运算，最后在协调节点进行统计，执行效率是可想而知的。目前，分库分表中间件，比较有代表性的是驱动层的 ShardingJdbc 和代理层的 MyCat，它们都有这样的问题。这些组件提供给使用者的视图是一致的，但我们在编码的时候，一定要注意这些区别。</p>
<h3>小结</h3>
<p>下面我们来总结一下。</p>
<p>本课时，我们简单看了一下 SpringBoot 常见的优化思路，然后介绍了三个新的性能分析工具。</p>
<ul>
<li>一个是监控系统 Prometheus，可以看到一些具体的指标大小；</li>
<li>一个是火焰图，可以看到具体的代码热点；</li>
<li>一个是 Skywalking，可以分析分布式环境中的调用链。</li>
</ul>
<p>SpringBoot 自身的 Web 容器是 Tomcat，那我们就可以通过对 Tomcat 的调优来获取性能提升。当然，对于服务上层的负载均衡 Nginx，我们也提供了一系列的优化思路。</p>
<p>最后，我们看了在经典的 MVC 架构下，Controller、Service、Dao 的一些优化方向，并着重看了 Service 层的分布式事务问题。</p>
<p>SpringBoot 作为一个广泛应用的服务框架，在性能优化方面已经做了很多工作，选用了很多高速组件。比如，数据库连接池默认使用 hikaricp，Redis 缓存框架默认使用 lettuce，本地缓存提供 caffeine 等。对于一个普通的数据库交互的 Web 服务来说，缓存是最主要的优化手段。</p>
<p>但细节决定成败，05-19 课时的内容对性能优化都有借鉴意义。下一课时（也就是咱们专栏的最后一课时），我将从问题发现、目标制定、优化方式上进行整体性的总结。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="19&#32;&#32;高级进阶：JVM&#32;常见优化参数.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="21&#32;&#32;性能优化的过程方法与求职面经总结.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script data-cfasync="false" src="../../cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script><script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434393f85a70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/Java%20%E6%80%A7%E8%83%BD%E4%BC%98%E5%8C%96%E5%AE%9E%E6%88%98-%E5%AE%8C/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
