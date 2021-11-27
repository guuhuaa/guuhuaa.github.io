<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>04  应用集成：在业务系统中使用 ShardingSphere 的方式有哪些？.md</title>
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

                    
                    <a href="00&#32;如何正确学习一款分库分表开源框架？.md">00 如何正确学习一款分库分表开源框架？.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;&#32;从理论到实践：如何让分库分表真正落地？.md">01  从理论到实践：如何让分库分表真正落地？.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;&#32;顶级项目：ShardingSphere&#32;是一款什么样的&#32;Apache&#32;开源软件？.md">02  顶级项目：ShardingSphere 是一款什么样的 Apache 开源软件？.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;&#32;规范兼容：JDBC&#32;规范与&#32;ShardingSphere&#32;是什么关系？.md">03  规范兼容：JDBC 规范与 ShardingSphere 是什么关系？.md</a>

                </li>
                <li>

                    <a class="current-tab" href="04&#32;&#32;应用集成：在业务系统中使用&#32;ShardingSphere&#32;的方式有哪些？.md">04  应用集成：在业务系统中使用 ShardingSphere 的方式有哪些？.md</a>
                    

                </li>
                <li>

                    
                    <a href="05&#32;&#32;配置驱动：ShardingSphere&#32;中的配置体系是如何设计的？.md">05  配置驱动：ShardingSphere 中的配置体系是如何设计的？.md</a>

                </li>
                <li>

                    
                    <a href="https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/ShardingSphere%20%E6%A0%B8%E5%BF%83%E5%8E%9F%E7%90%86%E7%B2%BE%E8%AE%B2-%E5%AE%8C/06%20%20%E6%95%B0%E6%8D%AE%E5%88%86%E7%89%87%EF%BC%9A%E5%A6%82%E4%BD%95%E5%AE%9E%E7%8E%B0%E5%88%86%E5%BA%93%E3%80%81%E5%88%86%E8%A1%A8%E3%80%81%E5%88%86%E5%BA%93+%E5%88%86%E8%A1%A8%E4%BB%A5%E5%8F%8A%E5%BC%BA%E5%88%B6%E8%B7%AF%E7%94%B1%EF%BC%9F%EF%BC%88%E4%B8%8A%EF%BC%89.md">06  数据分片：如何实现分库、分表、分库+分表以及强制路由？（上）.md</a>

                </li>
                <li>

                    
                    <a href="https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/ShardingSphere%20%E6%A0%B8%E5%BF%83%E5%8E%9F%E7%90%86%E7%B2%BE%E8%AE%B2-%E5%AE%8C/07%20%20%E6%95%B0%E6%8D%AE%E5%88%86%E7%89%87%EF%BC%9A%E5%A6%82%E4%BD%95%E5%AE%9E%E7%8E%B0%E5%88%86%E5%BA%93%E3%80%81%E5%88%86%E8%A1%A8%E3%80%81%E5%88%86%E5%BA%93+%E5%88%86%E8%A1%A8%E4%BB%A5%E5%8F%8A%E5%BC%BA%E5%88%B6%E8%B7%AF%E7%94%B1%EF%BC%9F%EF%BC%88%E4%B8%8B%EF%BC%89.md">07  数据分片：如何实现分库、分表、分库+分表以及强制路由？（下）.md</a>

                </li>
                <li>

                    
                    <a href="https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/ShardingSphere%20%E6%A0%B8%E5%BF%83%E5%8E%9F%E7%90%86%E7%B2%BE%E8%AE%B2-%E5%AE%8C/08%20%20%E8%AF%BB%E5%86%99%E5%88%86%E7%A6%BB%EF%BC%9A%E5%A6%82%E4%BD%95%E9%9B%86%E6%88%90%E5%88%86%E5%BA%93%E5%88%86%E8%A1%A8+%E6%95%B0%E6%8D%AE%E5%BA%93%E4%B8%BB%E4%BB%8E%E6%9E%B6%E6%9E%84%EF%BC%9F.md">08  读写分离：如何集成分库分表+数据库主从架构？.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;&#32;分布式事务：如何使用强一致性事务与柔性事务？.md">09  分布式事务：如何使用强一致性事务与柔性事务？.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;&#32;数据脱敏：如何确保敏感数据的安全访问？.md">10  数据脱敏：如何确保敏感数据的安全访问？.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;&#32;编排治理：如何实现分布式环境下的动态配置管理？.md">11  编排治理：如何实现分布式环境下的动态配置管理？.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;&#32;从应用到原理：如何高效阅读&#32;ShardingSphere&#32;源码？.md">12  从应用到原理：如何高效阅读 ShardingSphere 源码？.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;&#32;微内核架构：ShardingSphere&#32;如何实现系统的扩展性？.md">13  微内核架构：ShardingSphere 如何实现系统的扩展性？.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;&#32;分布式主键：ShardingSphere&#32;中有哪些分布式主键实现方式？.md">14  分布式主键：ShardingSphere 中有哪些分布式主键实现方式？.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;&#32;解析引擎：SQL&#32;解析流程应该包括哪些核心阶段？（上）.md">15  解析引擎：SQL 解析流程应该包括哪些核心阶段？（上）.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;&#32;解析引擎：SQL&#32;解析流程应该包括哪些核心阶段？（下）.md">16  解析引擎：SQL 解析流程应该包括哪些核心阶段？（下）.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;&#32;路由引擎：如何理解分片路由核心类&#32;ShardingRouter&#32;的运作机制？.md">17  路由引擎：如何理解分片路由核心类 ShardingRouter 的运作机制？.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;&#32;路由引擎：如何实现数据访问的分片路由和广播路由？.md">18  路由引擎：如何实现数据访问的分片路由和广播路由？.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;&#32;路由引擎：如何在路由过程中集成多种路由策略和路由算法？.md">19  路由引擎：如何在路由过程中集成多种路由策略和路由算法？.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;&#32;改写引擎：如何理解装饰器模式下的&#32;SQL&#32;改写实现机制？.md">20  改写引擎：如何理解装饰器模式下的 SQL 改写实现机制？.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;&#32;执行引擎：分片环境下&#32;SQL&#32;执行的整体流程应该如何进行抽象？.md">21  执行引擎：分片环境下 SQL 执行的整体流程应该如何进行抽象？.md</a>

                </li>
                <li>

                    
                    <a href="22&#32;&#32;执行引擎：如何把握&#32;ShardingSphere&#32;中的&#32;Executor&#32;执行模型？（上）.md">22  执行引擎：如何把握 ShardingSphere 中的 Executor 执行模型？（上）.md</a>

                </li>
                <li>

                    
                    <a href="23&#32;&#32;执行引擎：如何把握&#32;ShardingSphere&#32;中的&#32;Executor&#32;执行模型？（下）.md">23  执行引擎：如何把握 ShardingSphere 中的 Executor 执行模型？（下）.md</a>

                </li>
                <li>

                    
                    <a href="24&#32;&#32;归并引擎：如何理解数据归并的类型以及简单归并策略的实现过程？.md">24  归并引擎：如何理解数据归并的类型以及简单归并策略的实现过程？.md</a>

                </li>
                <li>

                    
                    <a href="25&#32;&#32;归并引擎：如何理解流式归并和内存归并在复杂归并场景下的应用方式？.md">25  归并引擎：如何理解流式归并和内存归并在复杂归并场景下的应用方式？.md</a>

                </li>
                <li>

                    
                    <a href="26&#32;&#32;读写分离：普通主从架构和分片主从架构分别是如何实现的？.md">26  读写分离：普通主从架构和分片主从架构分别是如何实现的？.md</a>

                </li>
                <li>

                    
                    <a href="27&#32;&#32;分布式事务：如何理解&#32;ShardingSphere&#32;中对分布式事务的抽象过程？.md">27  分布式事务：如何理解 ShardingSphere 中对分布式事务的抽象过程？.md</a>

                </li>
                <li>

                    
                    <a href="28&#32;&#32;分布式事务：ShardingSphere&#32;中如何集成强一致性事务和柔性事务支持？（上）.md">28  分布式事务：ShardingSphere 中如何集成强一致性事务和柔性事务支持？（上）.md</a>

                </li>
                <li>

                    
                    <a href="29&#32;&#32;分布式事务：ShardingSphere&#32;中如何集成强一致性事务和柔性事务支持？（下）.md">29  分布式事务：ShardingSphere 中如何集成强一致性事务和柔性事务支持？（下）.md</a>

                </li>
                <li>

                    
                    <a href="30&#32;&#32;数据脱敏：如何基于改写引擎实现低侵入性数据脱敏方案？.md">30  数据脱敏：如何基于改写引擎实现低侵入性数据脱敏方案？.md</a>

                </li>
                <li>

                    
                    <a href="31&#32;配置中心：如何基于配置中心实现配置信息的动态化管理？.md">31 配置中心：如何基于配置中心实现配置信息的动态化管理？.md</a>

                </li>
                <li>

                    
                    <a href="32&#32;注册中心：如何基于注册中心实现数据库访问熔断机制？.md">32 注册中心：如何基于注册中心实现数据库访问熔断机制？.md</a>

                </li>
                <li>

                    
                    <a href="33&#32;链路跟踪：如何基于&#32;Hook&#32;机制以及&#32;OpenTracing&#32;协议实现数据访问链路跟踪？.md">33 链路跟踪：如何基于 Hook 机制以及 OpenTracing 协议实现数据访问链路跟踪？.md</a>

                </li>
                <li>

                    
                    <a href="https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/ShardingSphere%20%E6%A0%B8%E5%BF%83%E5%8E%9F%E7%90%86%E7%B2%BE%E8%AE%B2-%E5%AE%8C/34%20%E7%B3%BB%E7%BB%9F%E9%9B%86%E6%88%90%EF%BC%9A%E5%A6%82%E4%BD%95%E5%AE%8C%E6%88%90%20ShardingSphere%20%E5%86%85%E6%A0%B8%E4%B8%8E%20Spring+SpringBoot%20%E7%9A%84%E6%97%A0%E7%BC%9D%E6%95%B4%E5%90%88%EF%BC%9F.md">34 系统集成：如何完成 ShardingSphere 内核与 Spring+SpringBoot 的无缝整合？.md</a>

                </li>
                <li>

                    
                    <a href="35&#32;结语：ShardingSphere&#32;总结及展望.md">35 结语：ShardingSphere 总结及展望.md</a>

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
                        <div><h1>04  应用集成：在业务系统中使用 ShardingSphere 的方式有哪些？</h1>
<p>在上一课时中，我详细介绍了 ShardingSphere 与 JDBC 规范之间的兼容性关系，我们知道 ShardingSphere 对 JDBC 规范进行了重写，并嵌入了分片机制。基于这种兼容性，开发人员使用 ShardingSphere 时就像在使用 JDBC 规范所暴露的各个接口一样。这一课时，我们将讨论如何在业务系统中使用 ShardingSphere 的具体方式。</p>
<h3>如何抽象开源框架的应用方式？</h3>
<p>当我们自己在设计和实现一款开源框架时，如何规划它的应用方式呢？作为一款与数据库访问相关的开源框架，ShardingSphere 提供了多个维度的应用方式，我们可以对这些应用方式进行抽象，从而提炼出一种模版。这个模版由四个维度组成，分别是<strong>底层工具、基础规范、开发框架和领域框架</strong>，如下图所示：</p>
<p><img src="assets/CgqCHl75qv-AFbZvAACz7F_yXRM280.png" alt="2.png" /></p>
<h4>底层工具</h4>
<p>底层工具指的是这个开源框架所面向的目标工具或所依赖的第三方工具。这种底层工具往往不是框架本身可以控制和管理的，框架的作用只是在它上面添加一个应用层，用于封装对这些底层工具的使用方式。</p>
<p>对于 ShardingSphere 而言，<strong>这里所说的底层工具实际上指的是关系型数据库</strong>。目前，ShardingSphere 支持包括 MySQL、Oracle、SQLServer、PostgreSQL 以及任何遵循 SQL92 标准的数据库。</p>
<h4>基础规范</h4>
<p>作为一个开源框架，很多时候需要兼容业界已经形成标准的基础性规范。换句话说，想要框架被其他开发人员所认可，就得要考虑开发人员目前在使用的基础规范。例如，如果设计一个与链路跟踪相关的开源框架，一般都需要兼容 OpenTracing 这一开放式分布式追踪规范。</p>
<p>对于 ShardingSphere 而言，所涉及的基础规范很明确，就是我们在上一课时中所详细阐述的 JDBC 规范。</p>
<h4>开发框架</h4>
<p>开源框架本身也是一个开发框架，但我们通常不会自己设计和实现一个全新的开发框架，而是更倾向于与现有的主流开发框架进行集成。目前，Java 世界中最主流的开发框架就是 Spring 家族系列框架。</p>
<p>ShardingSphere 同时集成了 Spring 和 Spring Boot 这两款 Spring 家族的主流开发框架。<strong>熟悉这两款框架的开发人员在应用 ShardingSphere 进行开发时将不需要任何学习成本</strong>。</p>
<h4>领域框架</h4>
<p>对于某些开源框架而言，也需要考虑和领域框架进行集成，以便提供更好的用户体验和使用友好性，区别于前面提到的适用于任何场景的开发框架。<strong>所谓领域框架，是指与所设计的开源框架属于同一专业领域的开发框架。</strong> 业务开发人员已经习惯在日常开发过程中使用这些特定于某一领域的开发框架，所以在设计自己的开源框架时，也需要充分考虑与这些框架的整合和集成。</p>
<p>对于 ShardingSphere 而言，领域框架指的是 MyBatis、Hibernate 等常见的 ORM 框架。ShardingSphere 对这领域框架提供了无缝集成的实现方案，熟悉 ORM 框架的开发人员在应用 ShardingSphere 进行开发时同样不需要任何学习成本。</p>
<p>接下来，我们就结合前面抽象的开源框架应用方式来具体分析 ShardingSphere 框架为开发人员提供了哪些开发上的支持。</p>
<h3>数据库和 JDBC 集成</h3>
<p>由于 ShardingSphere 最终操作的还是关系型数据库，并基于 JDBC 规范做了重写。所以<strong>在具体应用上相对比较简单，我们只要把握 JDBC 驱动和数据库连接池的使用方式即可。</strong></p>
<h4>JDBC 驱动</h4>
<p>ShardingSphere 支持 MySQL、Oracle 等实现 JDBC 规范的主流关系型数据库。我们在使用这些数据库时，常见的做法就是指定具体数据库对应的 JDBC 驱动类、URL 以及用户名和密码。</p>
<p>这里以 MySQL 为例，展示了在 Spring Boot 应用程序中通过 .yaml 配置文件指定 JDBC 驱动的一般做法：</p>
<pre><code>driverClassName: com.mysql.jdbc.Driver
url: jdbc:mysql://localhost:3306/test_database
username: root
password: root
</code></pre>
<h4>数据库连接池</h4>
<p>配置 JDBC 驱动的目的是获取访问数据库所需的 Connection。为了提高性能，主流做法是采用数据库连接池方案，数据库连接池将创建的 Connection 对象存放到连接池中，然后从池中提供 Connection。</p>
<p>ShardingSphere 支持一批主流的第三方数据库连接池，包括 DBCP、C3P0、BoneCP、Druid 和 HikariCP 等。在应用 ShardingSphere 时，我们可以通过创建 DataSource 来使用数据库连接池。例如，在 Spring Boot 中，可以在 .properties 配置文件中使用阿里巴巴提供的 DruidDataSource 类，初始化基于 Druid 数据库连接池的 DataSource：</p>
<pre><code>spring.shardingsphere.datasource.names= test_datasource
spring.shardingsphere.datasource.test_datasource.type=com.alibaba.druid.pool.DruidDataSource
spring.shardingsphere.datasource.test_datasource.driver-class-name=com.mysql.jdbc.Driver
spring.shardingsphere.datasource.test_datasource.jdbc-url=jdbc:mysql://localhost:3306/test_database
spring.shardingsphere.datasource.test_datasource.username=root
spring.shardingsphere.datasource.test_datasource.password=root
</code></pre>
<p>而对于使用 Spring 框架的开发人员而言，可以直接在 Spring 容器中注入一个 DruidDataSource 的 JavaBean：</p>
<pre><code>&lt;bean id=&quot;test_datasource&quot; class=&quot;com.alibaba.druid.pool.DruidDataSource&quot; destroy-method=&quot;close&quot;&gt;
    &lt;property name=&quot;driverClassName&quot; value=&quot;com.mysql.jdbc.Driver&quot;/&gt;
    &lt;property name=&quot;url&quot; value=&quot;jdbc:mysql://localhost:3306/ test_database&quot;/&gt;
    &lt;property name=&quot;username&quot; value=&quot;root&quot;/&gt;
    &lt;property name=&quot;password&quot; value=&quot;root&quot;/&gt;
&lt;/bean&gt;
</code></pre>
<h3>开发框架集成</h3>
<p>从上面所介绍的配置信息中，你实际上已经看到了 ShardingSphere 中集成的两款主流开发框架，即 Spring 和 Spring Boot，它们都对 JDBC 规范做了封装。当然，对于没有使用或无法使用 Spring 家族框架的场景，我们也可以直接在原生 Java 应用程序中使用 ShardingSphere。</p>
<p>在介绍开发框架的具体集成方式之前，我们来设计一个简单的应用场景。假设系统中存在一个用户表 User，这张表的数据量比较大，所以我们将它进行分库分表处理，计划分成两个数据库 ds0 和 ds1，然后每个库中再分成两张表 user0 和 user1：</p>
<p><img src="assets/Ciqc1F75qxSADY5yAADgZQ5r488284.png" alt="1.png" /></p>
<p>接下来，让我们来看一下如何基于 Java 原生、Spring 及 Spring Boot 开发框架针对这一场景实现分库分表。</p>
<h4>Java 原生</h4>
<p>如果使用 Java 原生的开发方式，相当于我们需要全部通过 Java 代码来创建和管理 ShardingSphere 中与分库分表相关的所有类。如果不做特殊说明，本课程将默认使用 Maven 实现包依赖关系的管理。所以，首先需要引入对 sharding-jdbc-core 组件的 Maven 引用：</p>
<pre><code>&lt;dependency&gt;
    &lt;groupId&gt;org.apache.shardingsphere&lt;/groupId&gt;
    &lt;artifactId&gt;sharding-jdbc-core&lt;/artifactId&gt;
&lt;/dependency&gt;
</code></pre>
<p>然后，按照 JDBC 的使用方法，需要创建 DataSource、Connection、Statement 等一系列接口的实现类，并通过这些类来完成具体的数据库访问操作。</p>
<p>我们先来看看创建 DataSource 的 Java 代码，这里构建了一个工具类 DataSourceHelper，基于 Druid 来获取一个 DruidDataSource：</p>
<pre><code>public final class DataSourceHelper{

    private static final String HOST = &quot;localhost&quot;;
    private static final int PORT = 3306;
    private static final String USER_NAME = &quot;root&quot;;
    private static final String PASSWORD = &quot;root&quot;;

    public static DataSource createDataSource(final String dataSourceName) {
        DruidDataSource result = new DruidDataSource();
        result.setDriverClassName(com.mysql.jdbc.Driver.class.getName());
        result.setUrl(String.format(&quot;jdbc:mysql://%s:%s/%s, HOST, PORT, dataSourceName));
        result.setUsername(USER_NAME);
        result.setPassword(PASSWORD);
        return result;
    }
}
</code></pre>
<p>由于在示例中，我们需要创建两个用户库，所以使用一个 Map 来保存两个数据源对象：</p>
<pre><code>    private static Map&lt;String, DataSource&gt; createDataSourceMap() {
        Map&lt;String, DataSource&gt; result = new HashMap&lt;&gt;();
        result.put(&quot;ds0&quot;, DataSourceHelper.createDataSource(&quot;ds0&quot;));
        result.put(&quot;ds1&quot;, DataSourceHelper.createDataSource(&quot;ds1&quot;));
        return result;
    }
</code></pre>
<p>有了包含初始化 DataSource 对象的数据源集合之后，接下来就可以通过设计分库分表规则来获取目标 DataSource：</p>
<pre><code>    public DataSource dataSource() throws SQLException {
         //创建分片规则配置类
        ShardingRuleConfiguration shardingRuleConfig = new ShardingRuleConfiguration();
        
        //创建分表规则配置类
        TableRuleConfiguration tableRuleConfig = new TableRuleConfiguration(&quot;user&quot;, &quot;ds${0..1}.user${0..1}&quot;);
        
        //创建分布式主键生成配置类
        Properties properties = new Properties();
        properties.setProperty(&quot;worker.id&quot;, &quot;33&quot;);
        KeyGeneratorConfiguration keyGeneratorConfig = new KeyGeneratorConfiguration(&quot;SNOWFLAKE&quot;, &quot;id&quot;, properties);              
        tableRuleConfig.setKeyGeneratorConfig(keyGeneratorConfig);      
        shardingRuleConfig.getTableRuleConfigs().add(tableRuleConfig);
        
        //根据性别分库，一共分为 2 个库
        shardingRuleConfig.setDefaultDatabaseShardingStrategyConfig(new InlineShardingStrategyConfiguration(&quot;sex&quot;, &quot;ds${sex % 2}&quot;));
        
        //根据用户 ID 分表，一共分为 2 张表
        shardingRuleConfig.setDefaultTableShardingStrategyConfig(new StandardShardingStrategyConfiguration(&quot;id&quot;, &quot;user${id % 2}&quot;));
        
        //通过工厂类创建具体的 DataSource
        return ShardingDataSourceFactory.createDataSource(createDataSourceMap(), shardingRuleConfig, new Properties());
    }
</code></pre>
<p>这里使用到了大量 ShardingSphere 中的规则配置类，包含分片规则配置、分表规则配置、分布式主键生成配置等。同时，我们在分片规则配置中使用行表达式来设置具体的分片规则。关于行表达式的具体使用方法将在下一课时中进行介绍，这里只简单地根据用户的年龄和 ID 分别来进行分库和分表。同时，我们在方法的最后部分传入前面已经初始化的 DataSource 集合并通过工厂类来创建具体的某一个目标 DataSource。</p>
<p>一旦获取了目标 DataSource 之后，我们就可以使用 JDBC 中的核心接口来执行传入的 SQL 语句：</p>
<pre><code>    List&lt;User&gt; getUsers(final String sql) throws SQLException {
        List&lt;User&gt; result = new LinkedList&lt;&gt;();
        try (Connection connection = dataSource.getConnection();
             PreparedStatement preparedStatement = connection.prepareStatement(sql);
             ResultSet resultSet = preparedStatement.executeQuery()) {
            while (resultSet.next()) {
                User user= new User();
                //省略设置User对象的赋值语句
                result.add(user);
            }
        }
        return result;
    }
</code></pre>
<p>可以看到，这里用到了熟悉的 Connection、PreparedStatement 和 ResultSet 等 JDBC 接口来执行查询并获取结果，整个过程就像是在使用普通的 JDBC 一样。但这个时候，这些 JDBC 接口背后的实现类都已经嵌入了分片功能。</p>
<h4>Spring</h4>
<p>如果使用 Spring 作为我们的开发框架，那么 JDBC 中各个核心对象的创建过程都会交给 Spring 容器进行完成。<strong>ShardingSphere 中基于命名空间（NameSpace）机制完成了与 Spring 框架的无缝集成。要想使用这种机制，需要先引入对应的 Maven 依赖</strong>：</p>
<pre><code>&lt;dependency&gt;
    &lt;groupId&gt;org.apache.shardingsphere&lt;/groupId&gt;
    &lt;artifactId&gt;sharding-jdbc-spring-namespace&lt;/artifactId&gt;
&lt;/dependency&gt;
</code></pre>
<p>Spring 中的命名空间机制本质上就是基于 Spring 配置文件的 XML Scheme 添加定制化的配置项并进行解析，所以我们会在 XML 配置文件中看到一系列与分片相关的自定义配置项。例如，DataSource 的初始化过程相当于创建一个 Java Bean 的过程：</p>
<pre><code>    &lt;bean id=&quot;ds0&quot; class=&quot;com.alibaba.druid.pool.DruidDataSource&quot;&gt;
        &lt;property name=&quot;driverClassName&quot; value=&quot;com.mysql.jdbc.Driver&quot;/&gt;
        &lt;property name=&quot;url&quot; value=&quot;jdbc:mysql://localhost:3306/ds0&quot;/&gt;
        &lt;property name=&quot;username&quot; value=&quot;root&quot;/&gt;
        &lt;property name=&quot;password&quot; value=&quot;root&quot;/&gt;
    &lt;/bean&gt;
</code></pre>
<p>接下来，我们同样可以通过一系列的配置项来初始化相应的分库规则，并最终完成目标 DataSource 的创建过程：</p>
<pre><code>    &lt;!-- 创建分库配置 --&gt;
    &lt;sharding:inline-strategy id=&quot;databaseStrategy&quot; sharding-column=&quot;sex&quot; algorithm-expression=&quot;ds${sex % 2}&quot; /&gt;

    &lt;!-- 创建分表配置 --&gt;
    &lt;sharding:inline-strategy id=&quot;tableStrategy&quot; sharding-column=&quot;id&quot; algorithm-expression=&quot;user${id % 2}&quot; /&gt;

    &lt;!-- 创建分布式主键生成配置 --&gt;
    &lt;bean:properties id=&quot;properties&quot;&gt;
        &lt;prop key=&quot;worker.id&quot;&gt;33&lt;/prop&gt;
    &lt;/bean:properties&gt;
    &lt;sharding:key-generator id=&quot;keyGenerator&quot; type=&quot;SNOWFLAKE&quot; column=&quot;id&quot; props-ref=&quot;properties&quot; /&gt;

    &lt;!-- 创建分片规则配置 --&gt;
    &lt;sharding:data-source id=&quot;shardingDataSource&quot;&gt;
        &lt;sharding:sharding-rule data-source-names=&quot;ds0, ds1&quot;&gt;
            &lt;sharding:table-rules&gt;
                &lt;sharding:table-rule logic-table=&quot;user&quot; actual-data-nodes=&quot;ds${0..1}.user${0..1}&quot; database-strategy-ref=&quot;databaseStrategy&quot; table-strategy-ref=&quot;tableStrategy&quot; key-generator-ref=&quot;keyGenerator&quot; /&gt;
            &lt;/sharding:table-rules&gt;
        &lt;/sharding:sharding-rule&gt;
    &lt;/sharding:data-source&gt;
</code></pre>
<p>关于这些配置项的内容我们同样放在下一课时中进行详细讨论。</p>
<h4>Spring Boot</h4>
<p>如果你使用的开发框架是 Spring Boot，那么所需要做的也是编写一些配置项。在 Spring Boot 中，配置项的组织形式有两种，一种是 .yaml 文件，一种是 .properties 文件，这里以 .properties 为例给出 DataSource 的配置：</p>
<pre><code>spring.shardingsphere.datasource.names=ds0,ds1 
spring.shardingsphere.datasource.ds0.type=com.alibaba.druid.pool.DruidDataSource
spring.shardingsphere.datasource.ds0.driver-class-name=com.mysql.jdbc.Driver
spring.shardingsphere.datasource.ds0.jdbc-url=jdbc:mysql://localhost:3306/ds0
spring.shardingsphere.datasource.ds0.username=root
spring.shardingsphere.datasource.ds0.password=root 
spring.shardingsphere.datasource.ds1.type=com.alibaba.druid.pool.DruidDataSource
spring.shardingsphere.datasource.ds1.driver-class-name=com.mysql.jdbc.Driver
spring.shardingsphere.datasource.ds1.jdbc-url=jdbc:mysql://localhost:3306/ds1
spring.shardingsphere.datasource.ds1.username=root
spring.shardingsphere.datasource.ds1.password=root
</code></pre>
<p>有了 DataSource 之后，我们同样可以设置对应的分库策略、分表策略及分布式主键生成策略：</p>
<pre><code>spring.shardingsphere.sharding.default-database-strategy.inline.sharding-column=sex
spring.shardingsphere.sharding.default-database-strategy.inline.algorithm-expression=ds$-&gt;{sex % 2} 
spring.shardingsphere.sharding.tables.user.actual-data-nodes=ds$-&gt;{0..1}.user$-&gt;{0..1}
spring.shardingsphere.sharding.tables.user.table-strategy.inline.sharding-column=id
spring.shardingsphere.sharding.tables.user.table-strategy.inline.algorithm-expression=user$-&gt;{id % 2}
spring.shardingsphere.sharding.tables.user.key-generator.column=id
spring.shardingsphere.sharding.tables.user.key-generator.type=SNOWFLAKE
spring.shardingsphere.sharding.tables.user.key-generator.props.worker.id=33
</code></pre>
<p>可以看到，相比 Spring 提供的命名空间机制，基于 Spring Boot 的配置风格相对简洁明了，容易理解。</p>
<p>一旦我们提供了这些配置项，就可以直接在应用程序中注入一个 DataSource 来获取 Connection 等 JDBC 对象。但在日常开发过程中，如果我们使用了 Spring 和 Spring Boot 开发框架，一般都不会直接使用原生的 JDBC 接口来操作数据库，而是通过集成常见的 ORM 框架来实现这一点。让我们来看一下。</p>
<h3>ORM 框架集成</h3>
<p>在 Java 领域，主流的 ORM 框架可以分成两大类，一类遵循 JPA（Java Persistence API，Java 持久层 API）规范，代表性的框架有 Hibernate、TopLink 等；而另一类则完全采用自定义的方式来实现对象和关系之间的映射，代表性的框架就是 MyBatis。</p>
<p>这里以 Spring Boot 开发框架为例，简要介绍这两种 ORM 框架的集成方式。基于 Spring Boot 提供的强大自动配置机制，我们发现集成这些 ORM 框架的方式非常简单。</p>
<h4>JPA</h4>
<p>想要在 Spring Boot 中使用 JPA，我们需要在 pom 文件中添加对 spring-boot-starter-data-jpa 的 Maven 依赖：</p>
<pre><code>&lt;dependency&gt;
       &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
      &lt;artifactId&gt;spring-boot-starter-data-jpa&lt;/artifactId&gt;
&lt;/dependency&gt;
</code></pre>
<p>一旦添加了 Maven 依赖，Spring Boot 就会自动导入 spring-orm、hibernate-entity-manager、spring-data-jpa 等一系列工具包。然后，在 application.properties 配置文件中添加与 JPA 相关的配置项就可以了：</p>
<pre><code>spring.jpa.properties.hibernate.hbm2ddl.auto=create-drop
spring.jpa.properties.hibernate.dialect=org.hibernate.dialect.MySQL5Dialect
spring.jpa.properties.hibernate.show_sql=false
</code></pre>
<p>当然，我们需要在业务代码中完成 JPA 的 Entity 实体类、Repository 仓库类的定义，并在 Spring Boot 的启动类中完成对包含对应包结构的扫描：</p>
<pre><code>@ComponentScan(&quot;com.user.jpa&quot;)
@EntityScan(basePackages = &quot;com.user.jpa.entity&quot;)
public class UserApplication
</code></pre>
<h4>MyBatis</h4>
<p>对于 MyBatis 而言，集成的步骤也类似。首先，我们需要添加 Maven 依赖：</p>
<pre><code>&lt;dependency&gt;
     &lt;groupId&gt;org.mybatis.spring.boot&lt;/groupId&gt;
     &lt;artifactId&gt;mybatis-spring-boot-starter&lt;/artifactId&gt;
&lt;/dependency&gt;
</code></pre>
<p>然后，由于 MyBatis 的启动依赖于框架提供的专用配置项，一般我们会把这些配置项组织在一个独立的配置文件中，并在 Spring Boot 的 application.properties 中引用这个配置文件：</p>
<pre><code>mybatis.config-location=classpath:META-INF/mybatis-config.xml
</code></pre>
<p>在 mybatis-config.xml 配置文件中，至少会包含各种 Mybatis Mapper 文件的定义：</p>
<pre><code>&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot; ?&gt;
&lt;!DOCTYPE configuration
        PUBLIC &quot;-//mybatis.org//DTD Config 3.0//EN&quot;
        &quot;http://mybatis.org/dtd/mybatis-3-config.dtd&quot;&gt;
&lt;configuration&gt;
    &lt;mappers&gt;
        &lt;mapper resource=&quot;mappers/UserMapper.xml&quot;/&gt;
    &lt;/mappers&gt;
&lt;/configuration&gt;
</code></pre>
<p>而在 Mapper 文件中，就包含了运行 MyBatis 所需的实体与数据库模式之间的映射关系，以及各种数据库操作的 SQL 语句定义。</p>
<p>最后，我们同样需要在 Spring Boot 的启动类中添加对包含各种 Entity 和 Repository 定义的包结构的扫描机制：</p>
<pre><code>@ComponentScan(&quot;com.user.mybatis&quot;)
@MapperScan(basePackages = &quot;com.user.mybatis.repository&quot;)
public class UserApplication
</code></pre>
<p>这样，我们在业务系统中使用 ShardingSphere 的各种方式就介绍完毕了。</p>
<h3>小结</h3>
<p>作为一个优秀的开源框架，ShardingSphere 提供了多方面的集成方式供广大开发人员在业务系统中使用它来完成分库分表操作。在这一课时中，我们先梳理了作为一个开源框架所应该具备的应用方式，并分析了这些应用方式在 ShardingSphere 中的具体实现机制。可以看到，<strong>从 JDBC 规范，到 Spring、Spring Boot 开发框架，再到 JPA、MyBatis 等主流 ORM 框架，ShardingSphere 都提供了完善的集成方案。</strong></p>
<p>这里给你留一道思考题：为了实现框架的易用性，ShardingSphere 为开发人员提供了哪些工具和规范的集成？</p>
<p>另一方面，在今天的课程中，我们也看到，使用 ShardingSphere 的主要方式事实上就是基于它所提供的配置体系，来完成各种配置项的创建和设置。可以说，配置工作是使用 ShardingSphere 进行开发的主要工作。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="03&#32;&#32;规范兼容：JDBC&#32;规范与&#32;ShardingSphere&#32;是什么关系？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="05&#32;&#32;配置驱动：ShardingSphere&#32;中的配置体系是如何设计的？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434c121e6270ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/ShardingSphere%20%E6%A0%B8%E5%BF%83%E5%8E%9F%E7%90%86%E7%B2%BE%E8%AE%B2-%E5%AE%8C/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
