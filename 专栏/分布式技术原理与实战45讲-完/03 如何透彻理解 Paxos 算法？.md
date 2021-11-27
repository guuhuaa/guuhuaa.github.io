<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>03 如何透彻理解 Paxos 算法？.md</title>
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

                    <a class="current-tab" href="03&#32;如何透彻理解&#32;Paxos&#32;算法？.md">03 如何透彻理解 Paxos 算法？.md</a>
                    

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
                        <div><h1>03 如何透彻理解 Paxos 算法？</h1>
<p>本课时我们主要讲解“如何透彻理解 Paxos 算法”？
Paxos 算法在分布式领域具有非常重要的地位，开源分布式锁组件 Google Chubby 的作者 Mike Burrows 说过，这个世界上只有一种一致性算法，那就是 Paxos 算法，其他的算法都是残次品。
Paxos 算法虽然重要，但是也因算法复杂而著名，不过 Paxos 算法是学习分布式系统必需的一个知识点，这一课时我们就知难而上，一起来学习下 Paxos 算法。</p>
<h1>Quorum 机制</h1>
<p>在学习 Paxos 算法之前，我们先来看分布式系统中的 Quorum 选举算法。在各种一致性算法中都可以看到Quorum 机制的身影，主要数学思想来源于抽屉原理，用一句话解释那就是，在 N 个副本中，一次更新成功的如果有 W 个，那么我在读取数据时是要从大于 N－W 个副本中读取，这样就能至少读到一个更新的数据了。
和 Quorum 机制对应的是 WARO，也就是Write All Read one，是一种简单的副本控制协议，当 Client 请求向某副本写数据时（更新数据），只有当所有的副本都更新成功之后，这次写操作才算成功，否则视为失败。
WARO 优先保证读服务，因为所有的副本更新成功，才能视为更新成功，从而保证了</p>
<p>所有的副本一致，这样的话，只需要读任何一个副本上的数据即可。写服务的可用性较低，因为只要有一个副本更新失败，此次写操作就视为失败了。假设有 N 个副本，N－1 个都宕机了，剩下的那个副本仍能提供读服务；但是只要有一个副本宕机了，写服务就不会成功。
WARO 牺牲了更新服务的可用性，最大程度地增强了读服务的可用性，而 Quorum 就是在更新服务和读服务之间进行的一个折衷。</p>
<h2>Quorum 定义</h2>
<p>Quorum 的定义如下：假设有 N 个副本，更新操作 wi 在 W 个副本中更新成功之后，才认为此次更新操作 wi 成功，把这次成功提交的更新操作对应的数据叫做：“成功提交的数据”。对于读操作而言，至少需要读 R 个副本才能读到此次更新的数据，其中，W+R&gt;N ，即 W 和 R 有重叠，一般，W+R=N+1。</p>
<blockquote>
<p><em>N = 存储数据副本的数量</em></p>
</blockquote>
<blockquote>
<p><em>W = 更新成功所需的副本</em></p>
</blockquote>
<blockquote>
<p><em>R = 一次数据对象读取要访问的副本的数量</em></p>
</blockquote>
<p>Quorum就是限定了一次需要读取至少N+1-w的副本数据,听起来有些抽象，举个例子，我们维护了10个副本，一次成功更新了三个，那么至少需要读取八个副本的数据，可以保证我们读到了最新的数据。</p>
<h2>Quorum 的应用</h2>
<p>Quorum 机制无法保证强一致性，也就是无法实现任何时刻任何用户或节点都可以读到最近一次成功提交的副本数据。
Quorum 机制的使用需要配合一个获取最新成功提交的版本号的 metadata 服务，这样可以确定最新已经成功提交的版本号，然后从已经读到的数据中就可以确认最新写入的数据。
Quorum 是分布式系统中常用的一种机制，用来保证数据冗余和最终一致性的投票算法，在 Paxos、Raft 和 ZooKeeper 的 Zab 等算法中，都可以看到 Quorum 机制的应用。</p>
<h1>Paxos 节点的角色和交互</h1>
<p>了解了 Quorum 机制，我们接下来学习 Paxos 算法，首先看一下 Paxos 算法中的节点角色和交互。</p>
<h2>Paxos 的节点角色</h2>
<p>在 Paxos 协议中，有三类节点角色，分别是 Proposer、Acceptor 和 Learner，另外还有一个 Client，作为产生议题者。
<img src="assets/Cgq2xl6MNF2AHbQiAABGDsfyB3s143.png" alt="img" />
上述三类角色只是逻辑上的划分，在工作实践中，一个节点可以同时充当这三类角色。</p>
<h3>Proposer 提案者</h3>
<p>Proposer 可以有多个，在流程开始时，Proposer 提出议案，也就是value，所谓 value，在工程中可以是任何操作，比如“修改某个变量的值为某个新值”，Paxos 协议中统一将这些操作抽象为 value。
不同的 Proposer 可以提出不同的甚至矛盾的 value，比如某个 Proposer 提议“将变量 X 设置为 1”，另一个 Proposer 提议“将变量 X 设置为 2”，但对同一轮 Paxos 过程，最多只有一个 value 被批准。</p>
<h3>Acceptor 批准者</h3>
<p>在集群中，Acceptor 有 N 个，Acceptor 之间完全对等独立，Proposer 提出的 value 必须获得超过半数（N/2+1）的 Acceptor 批准后才能通过。</p>
<h3>Learner 学习者</h3>
<p>Learner 不参与选举，而是学习被批准的 value，在Paxos中，Learner主要参与相关的状态机同步流程。</p>
<p>这里Leaner的流程就参考了Quorum 议会机制，某个 value 需要获得 W=N/2 + 1 的 Acceptor 批准，Learner 需要至少读取 N/2+1 个 Accpetor，最多读取 N 个 Acceptor 的结果后，才能学习到一个通过的 value。</p>
<h3>Client 产生议题者</h3>
<p>Client 角色，作为产生议题者，实际不参与选举过程，比如发起修改请求的来源等。</p>
<h2>Proposer 与 Acceptor 之间的交互</h2>
<p>Paxos 中， Proposer 和 Acceptor 是算法核心角色，Paxos 描述的就是在一个由多个 Proposer 和多个 Acceptor 构成的系统中，如何让多个 Acceptor 针对 Proposer 提出的多种提案达成一致的过程，而 Learner 只是“学习”最终被批准的提案。
Proposer 与 Acceptor 之间的交互主要有 4 类消息通信，如下图：
<img src="assets/Ciqah16MNF2Ad_j9AAA5-uz9BWI899.png" alt="img" />
这 4 类消息对应于 Paxos 算法的两个阶段 4 个过程，下面在分析选举过程时会讲到。</p>
<h1>Paxos 选举过程</h1>
<p>选举过程可以分为两个部分，准备阶段和选举阶段，可以查看下面的时序图：
<img src="assets/Cgq2xl6MNF2ASwyyAAE2bn8RiaM148.png" alt="img" /></p>
<h2>Phase 1 准备阶段</h2>
<p>Proposer 生成全局唯一且递增的 ProposalID，向 Paxos 集群的所有机器发送 Prepare 请求，这里不携带 value，只携带 N 即 ProposalID。
Acceptor 收到 Prepare 请求后，判断收到的 ProposalID 是否比之前已响应的所有提案的 N 大，如果是，则：</p>
<ul>
<li>在本地持久化 N，可记为 Max_N；</li>
<li>回复请求，并带上已经 Accept 的提案中 N 最大的 value，如果此时还没有已经 Accept 的提案，则返回 value 为空；</li>
<li>做出承诺，不会 Accept 任何小于 Max_N 的提案。
如果否，则不回复或者回复 Error。</li>
</ul>
<h2>Phase 2 选举阶段</h2>
<p>为了方便描述，我们把 Phase 2 选举阶段继续拆分为 P2a、P2b 和 P2c。</p>
<h3>P2a：Proposer 发送 Accept</h3>
<p>经过一段时间后，Proposer 收集到一些 Prepare 回复，有下列几种情况：</p>
<ul>
<li>若回复数量 &gt; 一半的 Acceptor 数量，且所有回复的 value 都为空时，则 Porposer 发出 accept 请求，并带上自己指定的 value。</li>
<li>若回复数量 &gt; 一半的 Acceptor 数量，且有的回复 value 不为空时，则 Porposer 发出 accept 请求，并带上回复中 ProposalID 最大的 value，作为自己的提案内容。</li>
<li>若回复数量 &lt;= 一半的 Acceptor 数量时，则尝试更新生成更大的 ProposalID，再转到准备阶段执行。</li>
</ul>
<h3>P2b：Acceptor 应答 Accept</h3>
<p>Accpetor 收到 Accpet 请求 后，判断：</p>
<ul>
<li>若收到的 N &gt;= Max_N（一般情况下是等于），则回复提交成功，并持久化 N 和 value；</li>
<li>若收到的 N &lt; Max_N，则不回复或者回复提交失败。</li>
</ul>
<h3>P2c: Proposer 统计投票</h3>
<p>经过一段时间后，Proposer 会收集到一些 Accept 回复提交成功的情况，比如：</p>
<ul>
<li>当回复数量 &gt; 一半的 Acceptor 数量时，则表示提交 value 成功，此时可以发一个广播给所有的 Proposer、Learner，通知它们已 commit 的 value；</li>
<li>当回复数量 &lt;= 一半的 Acceptor 数量时，则尝试更新生成更大的 ProposalID，转到准备阶段执行。</li>
<li>当收到一条提交失败的回复时，则尝试更新生成更大的 ProposalID，也会转到准备阶段执行。</li>
</ul>
<h1>Paxos 常见的问题</h1>
<p>关于Paxos协议，有几个常见的问题，简单介绍下。
<strong>1.如果半数以内的 Acceptor 失效，如何正常运行？</strong></p>
<p>在Paxos流程中，如果出现半数以内的 Acceptor 失效，可以分为两种情况：</p>
<p>第一种，如果半数以内的 Acceptor 失效时还没确定最终的 value，此时所有的 Proposer 会重新竞争提案，最终有一个提案会成功提交。</p>
<p>第二种，如果半数以内的 Acceptor 失效时已确定最终的 value，此时所有的 Proposer 提交前必须以最终的 value 提交，也就是Value实际已经生效，此值可以被获取，并不再修改。
<strong>2. Acceptor需要接受更大的N，也就是ProposalID有什么意义？</strong></p>
<p>这种机制可以防止其中一个Proposer崩溃宕机产生阻塞问题，允许其他Proposer用更大ProposalID来抢占临时的访问权。
<strong>3. 如何产生唯一的编号，也就是 ProposalID？</strong></p>
<p>在《Paxos made simple》论文中提到，唯一编号是让所有的 Proposer 都从不相交的数据集合中进行选择，需要保证在不同Proposer之间不重复，比如系统有 5 个 Proposer，则可为每一个 Proposer 分配一个标识 j(0~4)，那么每一个 Proposer 每次提出决议的编号可以为 5*i + j，i 可以用来表示提出议案的次数。</p>
<h2>总结</h2>
<p>这一课时分享了 Paxos 协议相关的知识点，Paxos 是经典的分布式协议，理解了它们以后，学习其他分布式协议会简单很多。</p>
<p>Paxos算法更重要的是理解过程，并不是要把各个流程都背下来，除了文中介绍的，相关的分支判断和选择场景还有很多，如果希望了解Paxos算法相关的推导和证明，我在最后附上了 Paxos 相关的几篇论文地址，感兴趣的同学可以去学习下：</p>
<ul>
<li><a href="https://lamport.azurewebsites.net/pubs/lamport-paxos.pdf">The PartTime Parliament</a></li>
<li><a href="https://lamport.azurewebsites.net/pubs/paxos-simple.pdf">Paxos Made Simple</a></li>
<li><a href="https://www.microsoft.com/en-us/research/publication/fast-paxos/">fast-paxos</a></li>
</ul>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="02&#32;不同数据一致性模型有哪些应用？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="04&#32;ZooKeeper&#32;如何保证数据一致性？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4350476f4a645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
