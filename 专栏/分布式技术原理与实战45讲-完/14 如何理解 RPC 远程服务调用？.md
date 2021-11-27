<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>14 如何理解 RPC 远程服务调用？.md</title>
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

                    <a class="current-tab" href="14&#32;如何理解&#32;RPC&#32;远程服务调用？.md">14 如何理解 RPC 远程服务调用？.md</a>
                    

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

                    
                    <a href="20&#32;ServiceMesh：服务网格有哪些应用？.md">20 ServiceMesh：服务网格有哪些应用？.md</a>

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
                        <div><h1>14 如何理解 RPC 远程服务调用？</h1>
<p>本课时主要讲解 RPC 远程服务调用相关的知识。</p>
<p>RPC 远程服务调用是分布式服务架构的基础，无论微服务设计上层如何发展，讨论服务治理都绕不开远程服务调用，那么如何理解 RPC、有哪些常见的 RPC 框架、实现一款 RPC 框架需要哪些技术呢？</p>
<h3>如何理解 RPC</h3>
<p>RPC（Remote Procedure Call）是一种进程间通信方式，百科给出的定义是这样的：“RPC（远程过程调用协议），它是一种通过网络从远程计算机程序上请求服务，而不需要了解底层网络技术的协议”。</p>
<p>RPC 允许程序调用另一个地址空间的过程或函数，而<strong>不用程序员显式编码这个远程调用的细节</strong>。即无论是调用本地接口/服务的还是远程的接口/服务，本质上编写的调用代码基本相同。</p>
<p>比如两台服务器 A、B，一个应用部署在 A 服务器上，想要调用 B 服务器上应用提供的函数或者方法，由于不在一个内存空间，则不能直接调用，这时候就可以应用 RPC 框架的实现来解决。</p>
<h3>RPC 如何实现</h3>
<p>早期的远程服务调用一般是通过 RMI 或 Hessian 等工具实现，以 Java RMI 为例，RMI 是 Java 语言中 RPC 的一种实现方式。</p>
<p>Java RMI（Java 远程方法调用，Java Remote Method Invocation）是 Java 编程语言里，一种用于实现远程过程调用的应用程序编程接口。应用 Java RMI，可以让某个 Java 虚拟机上的对象调用另一个 Java 虚拟机中的对象上的方法。</p>
<p>Java RMI 实现主要依赖 java.rmi 包下面的工具类，具体流程包括继承 Remote 实现远程接口，开发业务逻辑，创建 Server 并且注册远程对象，客户端创建 Client 调用远程方法等。关于 RMI 的实现细节，由于实际开发中很少应用，这里不展开讲解了。</p>
<p>以 Java RMI 为代表的的早期 RPC 实现起来比较繁琐，需要在代码中直接编码地址，并且不支持服务治理，比如无法对服务调用进行统计、无法梳理服务依赖情况、无法保证服务上下线时的稳定性等。随着分布式系统规模的增长，传统方式已经无法满足开发需求，于是诞生了一系列的 RPC 服务框架。</p>
<h3>RPC 框架代表</h3>
<p>开源社区里有许多优秀的 RPC 框架，比如常用的 Dubbo、Thrift、gRPC 等，下面简单介绍一下这几款组件。</p>
<h4>Apache Dubbo</h4>
<p>Dubbo 是阿里巴巴公司开源的一个高性能 Java 分布式服务框架，目前已经成为 Apache 顶级项目。Dubbo 可以通过高性能的 RPC 实现服务的输出和输入，支持服务治理，提供了控制台界面，可以独立应用，也可以和 Spring 框架无缝集成。</p>
<p>Dubbo 在设计中采用了微内核架构，基于对 Java SPI 机制的扩展实现，Dubbo 对分布式服务调用核心功能都开放了扩展点，包括服务调用的负载均衡策略、序列化协议、传输协议等，使用者都可以添加自定义实现。</p>
<p>Dubbo 在国内曾经拥有很高的人气，是微服务架构的首选，后来随着 Spring Cloud 的流行，社区一度停更，外部用户发布了 DubboX 等升级版本。最近，Dubbo 社区又重新活跃，更新后的 Dubbo 也发布了 3.0 预览版等，并且宣布会在未来的版本中支持更多特性，值得期待。</p>
<h4>Google 的 gRPC</h4>
<p>gRPC 是 Google 开发的高性能、通用的开源 RPC 框架，gRPC 使用 ProtoBuf 来定义服务，ProtoBuf 是 Google 开发的一种数据序列化协议，性能比较高，压缩和传输效率高，语法也比较简单。另外，gRPC 支持多种语言，并能够基于语言自动生成客户端和服务端功能库。</p>
<h4>Apache Thrift</h4>
<p>Thrift 起源于 Facebook，和 Dubbo 一样，后来被提交 Apache 基金会将 Thrift 作为一个开源项目。Facebook 创造 Thrift 的目的是为了解决 Facebook 各系统间大数据量的传输通信，以及系统间语言环境不同需要跨平台的问题。</p>
<p>Thrift 支持多种编程语言，如 Java、C++、Python、PHP、Ruby 等，可以在多种不同的语言之间通信。应用 Thrift，需要在一个语言无关的 IDL 文件里，定义数据类型和服务接口，然后生成用来构建 RPC 客户和服务器所需的代码。</p>
<p>Thrift 主要的优点是跨语言；缺点是，由于需要定义独立的 IDL 文件，如果对服务进行修改，当数据结构发生变化时，必须重新编辑 IDL 文件、重新编译和生成相关的代码，修改起来比较繁琐。</p>
<h4>微博 Motan</h4>
<p>Motan 是新浪微博开源的一个 Java RPC 框架，官方文档对外宣传在微博平台已经广泛应用，每天为数百个服务完成近千亿次的调用。</p>
<p>Motan 基于 Java 语言开发，设计和实现与 Dubbo 比较类似，包括服务提供者（RPC Server）、服务调用方（RPC Client）、服务注册中心（Registry）三个角色。服务端会向注册中心注册服务，消费端使用服务需要先向注册中心进行订阅，根据注册中心的返回列表与具体的 服务端建立连接，进行 RPC 通讯。当服务端发生变更的时候，注册中心也会同步变更，然后同步的通知到消费端。</p>
<p>Motan 也提供了服务治理的功能，包括服务的发现、服务的摘除、高可用及负载均衡。</p>
<h3>RPC 框架用到哪些技术</h3>
<p>了解了常见的 RPC 框架后，我们来看一下实现一个 RPC 框架需要哪些技术。</p>
<h4>如何建立通信</h4>
<p>实现分布式服务框架，首先要解决不同节点之间通讯的问题，需要在客户端和服务器之间建立 TCP 连接，远程过程调用的所有交换的数据都在这个连接里传输。</p>
<p>一般来说，建立通信可以使用成熟的网络通信框架，比如 Java 语言中的 Netty，这是一个优秀的网络通信框架。在 Dubbo、Motan 中都应用了 Netty。</p>
<h4>如何进行网络传输</h4>
<p>建立通信之后，节点之间数据传输采用什么协议，也就是选择什么样的二进制数据格式组织；传输的数据如何序列化和反序列化，比如在 Dubbo 中，传输协议默认使用 Dubbo 协议，序列化支持选择 Hessian、Kryo、Protobuf 等不同方式。</p>
<h4>如何进行服务注册和发现</h4>
<p>服务注册和发现，也就是服务寻址，以 Dubbo 为例，下图分布式服务典型的寻址和调用过程：</p>
<p><img src="assets/CgqCHl6-XeSAaqlXAAE2pEPLeB0026.png" alt="image.png" /></p>
<p>服务注册，需要服务提供者启动后主动把服务注册到注册中心，注册中心存储了该服务的 IP、端口、调用方式（协议、序列化方式）等信息。</p>
<p>服务发现，当服务消费者第一次调用服务时，会通过注册中心找到相应的服务提供方地址列表，并缓存到本地，以供后续使用。当消费者再次调用服务时，不会再去请求注册中心，而是直接通过负载均衡算法从 IP 列表中取一个服务提供者调用服务。</p>
<p>上面列举了一些分布式服务框架的实现要点，除了这些，还有很多技术细节，比如如何实现服务调用，RPC 框架如何和服务层交互，Java 中通过代理实现服务调用，那么代理对象如何解析请求参数、如何处理返回值等。</p>
<h3>总结</h3>
<p>这一课时分享了 RPC 远程服务调用的概念，介绍了常见的 RPC 框架实现，以及 RPC 框架需要关心哪些技术。通过本课时的学习，相信你对 RPC 相关技术有了一个初步认识，如果对其中某个框架感兴趣，你可以在课后找一些资料深入了解。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/%E5%88%86%E5%B8%83%E5%BC%8F%E6%8A%80%E6%9C%AF%E5%8E%9F%E7%90%86%E4%B8%8E%E5%AE%9E%E6%88%9845%E8%AE%B2-%E5%AE%8C/13%20%E5%88%86%E5%B8%83%E5%BC%8F%E4%BA%8B%E5%8A%A1%E8%80%83%E7%82%B9%E6%A2%B3%E7%90%86%20+%20%E9%AB%98%E9%A2%91%E9%9D%A2%E8%AF%95%E9%A2%98.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="15&#32;为什么微服务需要&#32;API&#32;网关？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b43507aed6d645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
