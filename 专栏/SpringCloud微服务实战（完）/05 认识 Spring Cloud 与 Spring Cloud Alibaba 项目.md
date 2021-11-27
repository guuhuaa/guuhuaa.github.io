<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>05 认识 Spring Cloud 与 Spring Cloud Alibaba 项目.md</title>
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

                    <a class="current-tab" href="05&#32;认识&#32;Spring&#32;Cloud&#32;与&#32;Spring&#32;Cloud&#32;Alibaba&#32;项目.md">05 认识 Spring Cloud 与 Spring Cloud Alibaba 项目.md</a>
                    

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

                    
                    <a href="15&#32;破解服务中共性问题的繁琐处理方式——接入&#32;API&#32;网关.md">15 破解服务中共性问题的繁琐处理方式——接入 API 网关.md</a>

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
                        <div><h1>05 认识 Spring Cloud 与 Spring Cloud Alibaba 项目</h1>
<p>前面我们已经粗略的将项目的骨架搭建完成，并初步引入一些基础支撑功能，为后续的开发打好基础。本篇将介绍 Spring Cloud 及 Spring Cloud Alibaba 两个项目，从理论角度作个整体性掌握，后续进入开发实战作好铺垫工作。 Spring Cloud Alibaba 是 Spring Cloud 的一个子项目，在介绍 Spring Cloud Alibaba 之前，先简单聊一聊 Spring Cloud 的情况。</p>
<h3>Spring Cloud 介绍</h3>
<p>Spring Cloud 官方文档地址：<a href="https://spring.io/projects/spring-cloud">https://spring.io/projects/spring-cloud</a></p>
<p>它是由很多个组件共同组成的一套微服务技术体系解决方案，目前最新版本是 Hoxton，它的版本并不是我们常见的大版本、小版本的数字形式，Spring Cloud 的版本规划是按伦敦地铁站的名称先后顺序来规划的，目的是为了更好的管理每个 Spring Cloud 子项目的版本，避免自己的版本与子项目的版本号混淆，所以要特别注意两个项目的版本对应情况，以免实际应用中产生不必要的麻烦。</p>
<p>随着新版本的迭代更新，有些低版本的 Spring Cloud 的不建议再应用于生产，比如 Brixton 和 Angel 两个版本在 2017 年已经寿终正寝。 <img src="assets/2020-05-05-021720.jpg" alt="img" /> （ Spring Cloud 与 Spring Boot 的版本对应情况，来源于官网） <img src="assets/2020-05-05-021722.jpg" alt="img" /> ( 某 Spring Cloud Greenwich 版本与子项目的版本对应情况 ) Spring Cloud 基于 Spring Boot 对外提供一整套的微服务架构体系的解决方案，包括配置管理、服务注册与服务发现、路由、端到端的调用、负载均衡、断路器、全局锁、分布式消息等，对于这些功能 Spring Cloud 提供了多种项目选择，可从官网的主要项目列表一窥端倪。 <img src="assets/2020-05-05-021726.jpg" alt="img" /> 看上图有个比较突出的子项目： Spring Cloud netflix，由 Netflix 开发后来又并入 Spring Cloud 大家庭，它主要提供的模块包括：服务发现、断路器和监控、智能路由、客户端负载均衡等。但随着 Spring Cloud 的迭代，不少 Netflix 的组件进行了维护模式，最明显的莫过于 Spring Cloud Gateway 的推出来替代旧有的 Zuul 组件，有项目加入，也会有老旧项目退出舞台，这也是产品迭代的正常节奏。</p>
<p>这些子项目，极大的丰富了 Spring Cloud 在微服务领域中应用范围，几乎无需要借助外部组件，以一已之力打造全生态的微服务架构，并与外部基础运维组件更好的融合在一起。</p>
<p>下面再介绍一个近两年出现的一个新生项目 ： Spring Cloud Alibaba。</p>
<h3>Spring Cloud Alibaba 介绍</h3>
<p>官网地址：<a href="https://github.com/alibaba/spring-cloud-alibaba">https://github.com/alibaba/spring-cloud-alibaba</a> 它是 Spring Cloud 的一个子项目，致力于提供微服务开发的一站式解决方案，项目包含开发分布式应用服务的必需组件，方便开发者通过 Spring Cloud 编程模型轻松使用这些组件来开发分布式应用服务，只需要添加一些注解和少量配置，就可以将 Spring Cloud 应用接入阿里分布式应用解决方案，通过阿里中间件来迅速搭建分布式应用系统。 项目特性见下图： <img src="assets/2020-05-05-021728.jpg" alt="img" /> 包括一些关键组件：</p>
<ul>
<li><strong>Sentinel</strong>：把流量作为切入点，从流量控制、熔断降级、系统负载保护等多个维度保护服务的稳定性。与 Netflix 的 Hystrix 组件类似，但实现方式上更为轻量。</li>
<li><strong>Nacos</strong>：一个更易于构建云原生应用的动态服务发现、配置管理和服务管理平台，同时具备了之前 Netflix Eureka 和 Spring Cloud Config 的功能，而且 UI 操作上更加人性化。</li>
<li><strong>RocketMQ</strong>：一款开源的分布式消息系统，基于高可用分布式集群技术，提供低延时的、高可靠的消息发布与订阅服务，目前已交由 Apache 组织维护。</li>
<li><strong>Dubbo</strong>：Apache Dubbo™ 是一款高性能 Java RPC 框架，自交由 Apache 组织孵化后，目前社区生态很活跃，产生形态越来越丰富。</li>
<li><strong>Seata</strong>：阿里巴巴开源产品，一个易于使用的高性能微服务分布式事务解决方案，由早期内部产品 Fescar 演变而来。</li>
</ul>
<blockquote>
<p>以上组件都是均是开源实现方案。下面提到的几个组件都是结合阿里云的产品形态完成的功能，后续的案例开发实战不引入商业产品，需要的小伙伴可以购买后拿到对应的 API 直接接入即可。</p>
</blockquote>
<ul>
<li><strong>Alibaba Cloud ACM</strong>：一款在分布式架构环境中对应用配置进行集中管理和推送的应用配置中心产品，与开源产品 Nacos 功能类似。</li>
<li><strong>Alibaba Cloud OSS</strong>: 阿里云对象存储服务（Object Storage Service，简称 OSS），是阿里云提供的海量、安全、低成本、高可靠的云存储服务。您可以在任何应用、任何时间、任何地点存储和访问任意类型的数据。</li>
<li><strong>Alibaba Cloud SchedulerX</strong>: 阿里中间件团队开发的一款分布式任务调度产品，提供秒级、精准、高可靠、高可用的定时（基于 Cron 表达式）任务调度服务。</li>
<li><strong>Alibaba Cloud SMS</strong>: 覆盖全球的短信服务，友好、高效、智能的互联化通讯能力，帮助企业迅速搭建客户触达通道。</li>
</ul>
<p>在使用过程中，版本问题同样需要关注。 <img src="assets/2020-05-05-021730.jpg" alt="img" />（截图来源于 Spring 官网）</p>
<h3>Spring Boot 介绍</h3>
<p>不管是 Spring Cloud 还是 Spring Cloud Alibaba 项目，都是基于 Spring Boot ，所以先将 Spring Boot 掌握后，才能更好的应用这两个项目。提供的大量的 starter 组件，更是方便我们快速的应用相应的功能，由于其内置了应用容器( Tomcat ，Jetty ，Undertow )，无须再构建成 war 文件去部署，并遵从约定优于配置的原则，高效开发应用。</p>
<blockquote>
<p>下面的链接是一份 Spring Boot 的全量参数配置，相信对你会有帮助。 <a href="https://docs.spring.io/spring-boot/docs/2.2.4.RELEASE/reference/html/appendix-application-properties.html">https://docs.spring.io/spring-boot/docs/2.2.4.RELEASE/reference/html/appendix-application-properties.html</a></p>
</blockquote>
<p>本篇介绍了课程中使用到的三个关键项目，这里只是做个简单的概念了解，后续将结合实际业务进入开发工作。采用 Spring Boot 构建项目，一般直接是 jar 的形式运行，但有些小伙伴还是有偏爱 war 包情况，哪用 Spring Boot 搭建的项目如何构建出 war 包呢？</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="04&#32;如何维护接口文档供外部调用——在线接口文档管理.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="06&#32;服务多不易管理如何破——服务注册与发现.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434e140f8470ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
