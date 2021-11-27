<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>20 ServiceMesh：服务网格有哪些应用？.md</title>
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

                    
                    <a href="00&#32;开篇词：搭建分布式知识体系，挑战高薪&#32;Offer.md">00 开篇词：搭建分布式知识体系，挑战高薪 Offer.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;如何证明分布式系统的&#32;CAP&#32;理论？.md">01 如何证明分布式系统的 CAP 理论？.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;不同数据一致性模型有哪些应用？.md">02 不同数据一致性模型有哪些应用？.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;如何透彻理解&#32;Paxos&#32;算法？.md">03 如何透彻理解 Paxos 算法？.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;ZooKeeper&#32;如何保证数据一致性？.md">04 ZooKeeper 如何保证数据一致性？.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;共识问题：区块链如何确认记账权？.md">05 共识问题：区块链如何确认记账权？.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;如何准备一线互联网公司面试？.md">06 如何准备一线互联网公司面试？.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;分布式事务有哪些解决方案？.md">07 分布式事务有哪些解决方案？.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;对比两阶段提交，三阶段协议有哪些改进？.md">08 对比两阶段提交，三阶段协议有哪些改进？.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;MySQL&#32;数据库如何实现&#32;XA&#32;规范？.md">09 MySQL 数据库如何实现 XA 规范？.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;如何在业务中体现&#32;TCC&#32;事务模型？.md">10 如何在业务中体现 TCC 事务模型？.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;分布式锁有哪些应用场景和实现？.md">11 分布式锁有哪些应用场景和实现？.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;如何使用&#32;Redis&#32;快速实现分布式锁？.md">12 如何使用 Redis 快速实现分布式锁？.md</a>

                </li>
                <li>

                    
                    <a href="https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/%E5%88%86%E5%B8%83%E5%BC%8F%E6%8A%80%E6%9C%AF%E5%8E%9F%E7%90%86%E4%B8%8E%E5%AE%9E%E6%88%9845%E8%AE%B2-%E5%AE%8C/13%20%E5%88%86%E5%B8%83%E5%BC%8F%E4%BA%8B%E5%8A%A1%E8%80%83%E7%82%B9%E6%A2%B3%E7%90%86%20+%20%E9%AB%98%E9%A2%91%E9%9D%A2%E8%AF%95%E9%A2%98.md">13 分布式事务考点梳理 + 高频面试题.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;如何理解&#32;RPC&#32;远程服务调用？.md">14 如何理解 RPC 远程服务调用？.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;为什么微服务需要&#32;API&#32;网关？.md">15 为什么微服务需要 API 网关？.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;如何实现服务注册与发现？.md">16 如何实现服务注册与发现？.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;如何实现分布式调用跟踪？.md">17 如何实现分布式调用跟踪？.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;分布式下如何实现配置管理？.md">18 分布式下如何实现配置管理？.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;容器化升级对服务有哪些影响？.md">19 容器化升级对服务有哪些影响？.md</a>

                </li>
                <li>

                    <a class="current-tab" href="20&#32;ServiceMesh：服务网格有哪些应用？.md">20 ServiceMesh：服务网格有哪些应用？.md</a>
                    

                </li>
                <li>

                    
                    <a href="21&#32;Dubbo&#32;vs&#32;Spring&#32;Cloud：两大技术栈如何选型？.md">21 Dubbo vs Spring Cloud：两大技术栈如何选型？.md</a>

                </li>
                <li>

                    
                    <a href="https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/%E5%88%86%E5%B8%83%E5%BC%8F%E6%8A%80%E6%9C%AF%E5%8E%9F%E7%90%86%E4%B8%8E%E5%AE%9E%E6%88%9845%E8%AE%B2-%E5%AE%8C/22%20%E5%88%86%E5%B8%83%E5%BC%8F%E6%9C%8D%E5%8A%A1%E8%80%83%E7%82%B9%E6%A2%B3%E7%90%86%20+%20%E9%AB%98%E9%A2%91%E9%9D%A2%E8%AF%95%E9%A2%98.md">22 分布式服务考点梳理 + 高频面试题.md</a>

                </li>
                <li>

                    
                    <a href="23&#32;读写分离如何在业务中落地？.md">23 读写分离如何在业务中落地？.md</a>

                </li>
                <li>

                    
                    <a href="24&#32;为什么需要分库分表，如何实现？.md">24 为什么需要分库分表，如何实现？.md</a>

                </li>
                <li>

                    
                    <a href="25&#32;存储拆分后，如何解决唯一主键问题？.md">25 存储拆分后，如何解决唯一主键问题？.md</a>

                </li>
                <li>

                    
                    <a href="26&#32;分库分表以后，如何实现扩容？.md">26 分库分表以后，如何实现扩容？.md</a>

                </li>
                <li>

                    
                    <a href="27&#32;NoSQL&#32;数据库有哪些典型应用？.md">27 NoSQL 数据库有哪些典型应用？.md</a>

                </li>
                <li>

                    
                    <a href="28&#32;ElasticSearch&#32;是如何建立索引的？.md">28 ElasticSearch 是如何建立索引的？.md</a>

                </li>
                <li>

                    
                    <a href="https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/%E5%88%86%E5%B8%83%E5%BC%8F%E6%8A%80%E6%9C%AF%E5%8E%9F%E7%90%86%E4%B8%8E%E5%AE%9E%E6%88%9845%E8%AE%B2-%E5%AE%8C/29%20%E5%88%86%E5%B8%83%E5%BC%8F%E5%AD%98%E5%82%A8%E8%80%83%E7%82%B9%E6%A2%B3%E7%90%86%20+%20%E9%AB%98%E9%A2%91%E9%9D%A2%E8%AF%95%E9%A2%98.md">29 分布式存储考点梳理 + 高频面试题.md</a>

                </li>
                <li>

                    
                    <a href="30&#32;消息队列有哪些应用场景？.md">30 消息队列有哪些应用场景？.md</a>

                </li>
                <li>

                    
                    <a href="31&#32;集群消费和广播消费有什么区别？.md">31 集群消费和广播消费有什么区别？.md</a>

                </li>
                <li>

                    
                    <a href="32&#32;业务上需要顺序消费，怎么保证时序性？.md">32 业务上需要顺序消费，怎么保证时序性？.md</a>

                </li>
                <li>

                    
                    <a href="33&#32;消息幂等：如何保证消息不被重复消费？.md">33 消息幂等：如何保证消息不被重复消费？.md</a>

                </li>
                <li>

                    
                    <a href="34&#32;高可用：如何实现消息队列的&#32;HA？.md">34 高可用：如何实现消息队列的 HA？.md</a>

                </li>
                <li>

                    
                    <a href="35&#32;消息队列选型：Kafka&#32;如何实现高性能？.md">35 消息队列选型：Kafka 如何实现高性能？.md</a>

                </li>
                <li>

                    
                    <a href="36&#32;消息队列选型：RocketMQ&#32;适用哪些场景？.md">36 消息队列选型：RocketMQ 适用哪些场景？.md</a>

                </li>
                <li>

                    
                    <a href="https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/%E5%88%86%E5%B8%83%E5%BC%8F%E6%8A%80%E6%9C%AF%E5%8E%9F%E7%90%86%E4%B8%8E%E5%AE%9E%E6%88%9845%E8%AE%B2-%E5%AE%8C/37%20%E6%B6%88%E6%81%AF%E9%98%9F%E5%88%97%E8%80%83%E7%82%B9%E6%A2%B3%E7%90%86%20+%20%E9%AB%98%E9%A2%91%E9%9D%A2%E8%AF%95%E9%A2%98.md">37 消息队列考点梳理 + 高频面试题.md</a>

                </li>
                <li>

                    
                    <a href="38&#32;不止业务缓存，分布式系统中还有哪些缓存？.md">38 不止业务缓存，分布式系统中还有哪些缓存？.md</a>

                </li>
                <li>

                    
                    <a href="39&#32;如何避免缓存穿透、缓存击穿、缓存雪崩？.md">39 如何避免缓存穿透、缓存击穿、缓存雪崩？.md</a>

                </li>
                <li>

                    
                    <a href="40&#32;经典问题：先更新数据库，还是先更新缓存？.md">40 经典问题：先更新数据库，还是先更新缓存？.md</a>

                </li>
                <li>

                    
                    <a href="41&#32;失效策略：缓存过期都有哪些策略？.md">41 失效策略：缓存过期都有哪些策略？.md</a>

                </li>
                <li>

                    
                    <a href="42&#32;负载均衡：一致性哈希解决了哪些问题？.md">42 负载均衡：一致性哈希解决了哪些问题？.md</a>

                </li>
                <li>

                    
                    <a href="43&#32;缓存高可用：缓存如何保证高可用？.md">43 缓存高可用：缓存如何保证高可用？.md</a>

                </li>
                <li>

                    
                    <a href="https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/%E5%88%86%E5%B8%83%E5%BC%8F%E6%8A%80%E6%9C%AF%E5%8E%9F%E7%90%86%E4%B8%8E%E5%AE%9E%E6%88%9845%E8%AE%B2-%E5%AE%8C/44%20%E5%88%86%E5%B8%83%E5%BC%8F%E7%BC%93%E5%AD%98%E8%80%83%E7%82%B9%E6%A2%B3%E7%90%86%20+%20%E9%AB%98%E9%A2%91%E9%9D%A2%E8%AF%95%E9%A2%98.md">44 分布式缓存考点梳理 + 高频面试题.md</a>

                </li>
                <li>

                    
                    <a href="45&#32;从双十一看高可用的保障方式.md">45 从双十一看高可用的保障方式.md</a>

                </li>
                <li>

                    
                    <a href="46&#32;高并发场景下如何实现系统限流？.md">46 高并发场景下如何实现系统限流？.md</a>

                </li>
                <li>

                    
                    <a href="47&#32;降级和熔断：如何增强服务稳定性？.md">47 降级和熔断：如何增强服务稳定性？.md</a>

                </li>
                <li>

                    
                    <a href="48&#32;如何选择适合业务的负载均衡策略？.md">48 如何选择适合业务的负载均衡策略？.md</a>

                </li>
                <li>

                    
                    <a href="49&#32;线上服务有哪些稳定性指标？.md">49 线上服务有哪些稳定性指标？.md</a>

                </li>
                <li>

                    
                    <a href="50&#32;分布式下有哪些好用的监控组件？.md">50 分布式下有哪些好用的监控组件？.md</a>

                </li>
                <li>

                    
                    <a href="51&#32;分布式下如何实现统一日志系统？.md">51 分布式下如何实现统一日志系统？.md</a>

                </li>
                <li>

                    
                    <a href="52&#32;分布式路漫漫，厚积薄发才是王道.md">52 分布式路漫漫，厚积薄发才是王道.md</a>

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
                        <div><h1>20 ServiceMesh：服务网格有哪些应用？</h1>
<p>微服务的部署架构中有一个有趣的边车模式，并且基于边车模式，扩展出了 Service Mesh 服务网格的概念。这一课时我们一起来学习下 Service Mesh 相关的知识。</p>
<h3>Sidecar 设计模式</h3>
<p>在了解服务网格之前，先来看一个微服务的设计模式——Sidecar，也就是边车模式。边车模式是一种分布式服务架构的设计模式，特别是在各大云服务厂商中应用较多。</p>
<p>边车模式因为类似于生活中的边三轮摩托车而得名，也就是侉子摩托车。边三轮摩托车是给摩托车加装一个挎斗，可以装载更多的货物，变得更加多用途，得益于这样的特性，边三轮摩托曾经得到了广泛应用。</p>
<p>在系统设计时，边车模式通过给应用程序添加边车的方式来拓展应用程序现有的功能，分离通用的业务逻辑，比如日志记录、流量控制、服务注册和发现、限流熔断等功能。通过添加边车实现，微服务只需要专注实现业务逻辑即可，实现了控制和逻辑的分离与解耦。</p>
<p>边车模式中的边车，实际上就是一个 Agent，微服务的通信可以通过 Agent 代理完成。在部署时，需要同时启动 Agent，Agent 会处理服务注册、服务发现、日志和服务监控等逻辑。这样在开发时，就可以忽略这些和对外业务逻辑本身没有关联的功能，实现更好的内聚和解耦。</p>
<p>应用边车模式解耦了服务治理和对外的业务逻辑，这一点和 API 网关比较像，但是边车模式控制的粒度更细，可以直接接管服务实例，合理扩展边车的功能，能够实现服务的横向管理，提升开发效率。</p>
<h3>Service Mesh 服务网格</h3>
<p>在边车模式中，可以实现服务注册和发现、限流熔断等功能。如果边车的功能可以进一步标准化，那么会变得更加通用，就可以抽象出一个通用的服务治理组件，通过边车与其他系统交互，在各个微服务中进行推广。</p>
<p>随着分布式服务的发展，类似的需求越来越多，就出现了服务网格的概念。</p>
<h4>什么是 Service Mesh</h4>
<p>微服务领域有 CNCF 组织（Cloud Native Computing Foundation），也就是云原生基金会，CNCF 致力于微服务开源技术的推广。Service Mesh 是 CNCF 推广的新一代微服务架构，致力于解决服务间通讯。</p>
<p>Service Mesh 基于边车模式演进，通过在系统中添加边车代理，也就是 Sidecar Proxy 实现。</p>
<p><img src="assets/Ciqc1F7YqhyAVsPfAAF3tkypmzU109.png" alt="image.png" /></p>
<p>Service Mesh 可以认为是边车模式的进一步扩展，提供了以下功能：</p>
<ul>
<li>管理服务注册和发现</li>
<li>提供限流和降级功能</li>
<li>前置的负载均衡</li>
<li>服务熔断功能</li>
<li>日志和服务运行状态监控</li>
<li>管理微服务和上层容器的通信</li>
</ul>
<h4>Service Mesh 有哪些特点</h4>
<p>使用 Sidecar 或者 Service Mesh，都可以认为是在原有的系统之上抽象了一层新的设计来实现。计算机领域有这么一句话：没有什么系统问题不是抽象一层解决不了的，如果有，那就再抽象一层。</p>
<p>Service Mesh 服务网格就是使用了这样的思想，抽象出专门的一层，提供服务治理领域所需的服务注册发现、负载均衡、熔断降级、监控等功能。现在的微服务有很多部署在各大云服务厂商的主机上，不同厂商的实现标准不同，如何更好地基于各类云服务部署业务系统，这也是云原生要解决的问题。</p>
<p>Service Mesh 可以统一管理微服务与上层通信的部分，接管各种网络通信、访问控制等，我们的业务代码只需要关心业务逻辑就可以，简化开发工作。</p>
<h4>Service Mesh 和 API 网关的区别</h4>
<p>服务网格实现的功能和 API 网关类似，都可以以一个切面的形式，进行一些横向功能的实现，比如流量控制、访问控制、日志和监控等功能。</p>
<p>服务网格和 API 网关主要的区别是部署方式不同，在整体系统架构中的位置不一样。</p>
<p>API 网关通常是独立部署，通过单独的系统提供服务，为了实现高可用，还会通过网关集群等来管理；而服务网格通常是集成在应用容器内的，服务网格离应用本身更近，相比 API 网关，和应用交互的链路更短，所以可以实现更细粒度的应用管理，也体现了 Sidecar 边车的设计思想。</p>
<h3>Service Mesh 解决方案</h3>
<p>目前两款流行的 Service Mesh 开源软件分别是 Istio 和 Linkerd，下面简单介绍。</p>
<h4>Istio</h4>
<p>Istio 是 Google、IBM 等几大公司联合开源的一个服务网格组件，Istio 提供了负载均衡、服务间的身份验证、监控等方法。</p>
<p>Istio 的实现是通过 Sidecar ，通过添加一个 Sidecar 代理，在环境中为服务添加 Istio 的支持。Istio 代理会拦截不同服务之间的通信，然后进行统一的配置和管理。</p>
<p>官方文档中，对 Istio 支持的特性描述如下：</p>
<ul>
<li>为 HTTP、gRPC、WebSocket 和 TCP 流量自动负载均衡；</li>
<li>对流量行为进行细粒度控制，包括丰富的路由规则、重试、故障转移和故障注入；</li>
<li>可插拔的策略层和配置 API，支持访问控制、速率限制和配额；</li>
<li>管理集群内所有流量的自动化度量、日志记录和追踪；</li>
<li>实现安全的服务间通信，支持基于身份验证和授权的集群。</li>
</ul>
<p>Istio 官网开放了中文用户指南，可以点击链接查看 <a href="https://istio.io/zh/docs/">https://istio.io/zh/docs/</a>，翻译质量一般，感兴趣的同学建议直接查看英文手册。</p>
<h4>Linkerd</h4>
<p>Linkerd 最早由 Twitter 贡献，支持的功能和 Istio 类似，Linkerd 是一款开源网络代理，可以作为服务网格进行部署，在应用程序内管理和控制服务与服务之间的通信。</p>
<p>Linkerd 出现来自 Linkerd 团队为 Twitter、Yahoo、Google 和 Microsoft 等公司运营大型生产系统时发现：最复杂和令人惊讶的问题来源通常不是服务本身，而是服务之间的通讯。Linkerd 目标是解决服务之间的通信问题，通过添加 Linkerd 代理，实现一个专用的基础设施层，为应用提供服务发现、路由、错误处理及服务可见性等功能，而无须侵入应用内部实现。</p>
<p>Istio 和 Linkerd 都处于快速发展阶段，可以到 Istio 和 Linkerd 的官网了解更多的信息。国内也有一些技术小组在进行相关的文档翻译工作，有意向的同学可以加入。</p>
<h3>总结</h3>
<p>这一课时和你分享了 Service Mesh 服务网格相关的内容，包括微服务中的边车模式，服务网格发展，最后简单介绍了目前流行的两种服务网格解决方案。</p>
<p>Service Mesh 作为一个比较新的领域，可以帮助我们了解微服务架构发展的方向，特别是解决服务上云，以及云原生等问题，对云原生等话题感兴趣的同学，可以关注下平台内的其他专栏。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="19&#32;容器化升级对服务有哪些影响？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="21&#32;Dubbo&#32;vs&#32;Spring&#32;Cloud：两大技术栈如何选型？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4350999832645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/%E5%88%86%E5%B8%83%E5%BC%8F%E6%8A%80%E6%9C%AF%E5%8E%9F%E7%90%86%E4%B8%8E%E5%AE%9E%E6%88%9845%E8%AE%B2-%E5%AE%8C/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
