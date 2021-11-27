<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>05  配置驱动：ShardingSphere 中的配置体系是如何设计的？.md</title>
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

                    
                    <a href="04&#32;&#32;应用集成：在业务系统中使用&#32;ShardingSphere&#32;的方式有哪些？.md">04  应用集成：在业务系统中使用 ShardingSphere 的方式有哪些？.md</a>

                </li>
                <li>

                    <a class="current-tab" href="05&#32;&#32;配置驱动：ShardingSphere&#32;中的配置体系是如何设计的？.md">05  配置驱动：ShardingSphere 中的配置体系是如何设计的？.md</a>
                    

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
                        <div><h1>05  配置驱动：ShardingSphere 中的配置体系是如何设计的？</h1>
<p>在上一课时中，我们介绍了在业务系统中应用 ShardingSphere 的几种方法。事实上，我们发现，除了掌握 Spring、Spring Boot、Mybatis 等常见框架的功能特性之外，使用 ShardingSphere 的主要工作在于根据业务需求完成各种分片操作相关配置项的设置。今天，我就来带领你剖析 ShardingSphere 中的配置体系到底是如何进行设计并实现的，这也是我们介绍 ShardingSphere 核心功能的前提。</p>
<h3>什么是行表达式？</h3>
<p>在引入配置体系的学习之前，我们先来介绍 ShardingSphere 框架为开发人员提供的一个辅助功能，这个功能就是行表达式。</p>
<p><strong>行表达式是 ShardingSphere 中用于实现简化和统一配置信息的一种工具，在日常开发过程中应用得非常广泛。</strong> 它的使用方式非常直观，只需要在配置中使用 ${expression} 或 $-&gt;{expression} 表达式即可。</p>
<p>例如上一课时中使用的&quot;ds${0..1}.user${0..1}&quot;就是一个行表达式，用来设置可用的数据源或数据表名称。基于行表达式语法，${begin..end} 表示的是一个从&quot;begin&quot;到&quot;end&quot;的范围区间，而多个 ${expression} 之间可以用&quot;.&quot;符号进行连接，代表多个表达式数值之间的一种笛卡尔积关系。这样，如果采用图形化的表现形式，&quot;ds${0..1}.user${0..1}&quot;表达式最终会解析成这样一种结果：</p>
<p><img src="assets/CgqCHl75rReAY_fbAACRt1sYKS0524.png" alt="image" /></p>
<p>当然，类似场景也可以使用枚举的方式来列举所有可能值。行表达式也提供了 ${[enum1, enum2,…, enumx]} 语法来表示枚举值，所以&quot;ds${0..1}.user${0..1}&quot;的效果等同于&quot;ds${[0,1]}.user${[0,1]}&quot;。</p>
<p>同样，在上一课时中使用到的 ds${age % 2} 表达式，它表示根据 age 字段进行对 2 取模，从而自动计算目标数据源是 ds0 还是 ds1。所以，除了配置数据源和数据表名称之外，行表达式在 ShardingSphere 中另一个常见的应用场景就是配置各种分片算法，我们会在后续的示例中大量看到这种使用方法。</p>
<p>由于 ${expression} 与 Spring 本身的属性文件占位符冲突，而 Spring 又是目前主流的开发框架，因此在正式环境中建议你使用 $-&gt;{expression} 来进行配置。</p>
<h3>ShardingSphere 有哪些核心配置？</h3>
<p>对于分库分表、读写分离操作而言，配置的主要任务是完成各种规则的创建和初始化。配置是整个 ShardingSphere 的核心，也是我们在日常开发过程中的主要工作。可以说，只要我们掌握了 ShardingSphere 的核心配置项，就相当于掌握了这个框架的使用方法。那么，ShardingSphere 有哪些核心配置呢？这里以分片引擎为例介绍最常用的几个配置项，而与读写分离、数据脱敏、编排治理相关的配置项我们会在介绍具体的应用场景时再做展开。</p>
<h4>ShardingRuleConfiguration</h4>
<p>我们在上一课时中已经了解了如何通过框架之间的集成方法来创建一个 DataSource，这个 DataSource 就是我们使用 ShardingSphere 的入口。我们也看到在创建 DataSource 的过程中使用到了一个 ShardingDataSourceFactory 类，这个工厂类的构造函数中需要传入一个 ShardingRuleConfiguration 对象。显然，从命名上看，这个 ShardingRuleConfiguration 就是用于分片规则的配置入口。</p>
<p>ShardingRuleConfiguration 中所需要配置的规则比较多，我们可以通过一张图例来进行简单说明，在这张图中，我们列举了每个配置项的名称、类型以及个数关系：</p>
<p><img src="assets/Ciqc1F75rTaADRO6AAD5MCLrohA562.png" alt="image" /></p>
<p>这里引入了一些新的概念，包括绑定表、广播表等，这些概念在下一课时介绍到 ShardingSphere 的分库分表操作时都会详细展开，这里不做具体介绍。<strong>事实上，对于 ShardingRuleConfiguration 而言，必须要设置的只有一个配置项，即 TableRuleConfiguration。</strong></p>
<h4>TableRuleConfiguration</h4>
<p>从命名上看，TableRuleConfiguration 是表分片规则配置，但事实上，这个类同时包含了对分库和分表两种场景的设置。TableRuleConfiguration 包含很多重要的配置项：</p>
<ul>
<li>actualDataNodes</li>
</ul>
<p>actualDataNodes 代表真实的数据节点，由数据源名+表名组成，支持行表达式。例如，前面介绍的&quot;ds${0..1}.user${0..1}&quot;就是比较典型的一种配置方式。</p>
<ul>
<li>databaseShardingStrategyConfig</li>
</ul>
<p>databaseShardingStrategyConfig 代表分库策略，如果不设置则使用默认分库策略，这里的默认分库策略就是 ShardingRuleConfiguration 中的 defaultDatabaseShardingStrategyConfig 配置。</p>
<ul>
<li>tableShardingStrategyConfig</li>
</ul>
<p>和 databaseShardingStrategyConfig 一样，tableShardingStrategyConfig 代表分表策略，如果不设置也会使用默认分表策略，这里的默认分表策略同样来自 ShardingRuleConfiguration 中的 defaultTableShardingStrategyConfig 配置。</p>
<ul>
<li>keyGeneratorConfig</li>
</ul>
<p>keyGeneratorConfig 代表分布式环境下的自增列生成器配置，ShardingSphere 中集成了雪花算法等分布式 ID 的生成器实现。</p>
<h4>ShardingStrategyConfiguration</h4>
<p>我们注意到，databaseShardingStrategyConfig 和 tableShardingStrategyConfig 的类型都是一个 ShardingStrategyConfiguration 对象。在 ShardingSphere 中，ShardingStrategyConfiguration 实际上是一个空接口，存在一系列的实现类，其中的每个实现类都代表一种分片策略：</p>
<p><img src="assets/CgqCHl75rUiACYZ1AAA8JV6ve54396.png" alt="3.png" />
　ShardingStrategyConfiguration 的类层结构图</p>
<p>在这些具体的分片策略中，通常需要指定一个分片列 shardingColumn 以及一个或多个分片算法 ShardingAlgorithm。当然也有例外，例如 HintShardingStrategyConfiguration 直接使用数据库的 Hint 机制实现强制路由，所以不需要分片列。我们会在《路由引擎：如何在路由过程中集成多种分片策略和分片算法？》中对这些策略的实现过程做详细的剖析。</p>
<h4>KeyGeneratorConfiguration</h4>
<p>可以想象，对于一个自增列而言，KeyGeneratorConfiguration 中首先需要指定一个列名 column。同时，因为 ShardingSphere 中内置了一批自增列的实现机制（例如雪花算法 SNOWFLAKE 以及通用唯一识别码 UUID），所以需要通过一个 type 配置项进行指定。最后，我们可以利用 Properties 配置项来指定自增值生成过程中所需要的相关属性配置。关于这一点，我们在上一课时中也看到了示例，即雪花算法中配置 workerId 为 33。</p>
<p>基于以上核心配置项，我们已经可以完成日常开发过程中常见的分库分表操作。当然，对于不同的开发人员，如何采用某一个特定的方式将这些配置项信息集成到业务代码中，也存在着不同的诉求。因此，ShardingSphere 中也提供了一系列的配置方式供开发人员进行选择。</p>
<h3>ShardingSphere 提供了哪些配置方式？</h3>
<p>从 Java 代码到配置文件，ShardingSphere 提供了 4 种配置方式，用于不同的使用场景，分别是：</p>
<ul>
<li>Java 代码配置</li>
<li>Yaml 配置</li>
<li>Spring 命名空间配置</li>
<li>Spring Boot配置</li>
</ul>
<p>我们来看一下这四种配置的具体方法。</p>
<h4>Java 代码配置</h4>
<p>Java 代码配置是使用 ShardingSphere 所提供的底层 API 来完成配置系统构建的原始方式。在上一课时中，我们已经看到了如何初始化 ShardingRuleConfiguration 和 TableRuleConfiguration 类，并通过 ShardingDataSourceFactory 创建目标 DataSource 的具体方式，这里不再展开。</p>
<p>在日常开发中，我们一般不会直接使用 Java 代码来完成 ShardingSphere 配置体系的构建。一方面，如果使用 Java 代码来实现配置，一旦有变动就需要重新编译代码并发布，不利于实现配置信息的动态化管理和系统的持续集成。另一方面，代码级别的配置方式也比较繁琐，不够直接且容易出错，维护性也不好。</p>
<p>当然，也可能有例外情况。一种情况是，如果我们需要和其他框架进行更加底层的集成或定制化开发时，往往只能采用 Java 代码才能达到理想的效果。同时，对于刚接触 ShardingSphere 的开发人员而言，基于框架提供的 API 进行开发更加有利于快速掌握框架提供的各种类之间的关联关系和类层结构。</p>
<h4>Yaml 配置</h4>
<p>Yaml 配置是 ShardingSphere 所推崇的一种配置方式。Yaml 的语法和其他高级语言类似，并且可以非常直观地描述多层列表和对象等数据形态，特别适合用来表示或编辑数据结构和各种配置文件。</p>
<p>在语法上，常见的&quot;!!&quot;表示实例化该类；以&quot;-&quot;开头的多行构成一个数组；以&quot;:&quot;表示键值对；以&quot;#&quot;表示注释。关于 Yaml 语法的更多介绍可以参考百度百科 <a href="https://baike.baidu.com/item/YAML">https://baike.baidu.com/item/YAML</a>。<strong>请注意，Yaml 大小写敏感，并使用缩进表示层级关系。</strong> 这里给出一个基于 ShardingSphere 实现读写分离场景下的配置案例：</p>
<pre><code>dataSources:
  dsmaster: !!com.alibaba.druid.pool.DruidDataSource
    driverClassName: com.mysql.jdbc.Driver
    url: jdbc:mysql://119.3.52.175:3306/dsmaster
    username: root
    password: root
  dsslave0: !!com.alibaba.druid.pool.DruidDataSource
    driverClassName: com.mysql.jdbc.Driver
    url: jdbc:mysql://119.3.52.175:3306/dsslave0
    username: root
    password: root
  dsslave1: !!com.alibaba.druid.pool.DruidDataSource
    driverClassName: com.mysql.jdbc.Driver
    url: jdbc:mysql://119.3.52.175:3306/dsslave1
    username: root
    password: root 
masterSlaveRule:
  name: health_ms
  masterDataSourceName: dsmaster
  slaveDataSourceNames: [dsslave0, dsslave1]
</code></pre>
<p>可以看到，这里配置了 dsmaster、dsslave0 和 dsslave1 这三个 DataSource，然后针对每个 DataSource 分别设置了它们的驱动信息。最后，基于这三个 DataSource 配置了一个 masterSlaveRule 规则，用于指定具体的主从架构。</p>
<p>在 ShardingSphere 中，我们可以把配置信息存放在一个 .yaml 配置文件中，并通过加载这个配置文件来完成配置信息的解析。这种机制为开发人员高效管理配置信息提供了更多的灵活性和可定制性。在今天内容的最后，我们会详细剖析这一机制的实现原理。</p>
<h4>Spring 命名空间配置</h4>
<p>我们可以通过自定义配置标签实现方案来扩展 Spring 的命名空间，从而在 Spring 中嵌入各种自定义的配置项。Spring 框架从 2.0 版本开始提供了基于 XML Schema 的风格来定义 Javabean 的扩展机制。通过 XML Schema 的定义，把一些原本需要通过复杂的 Javabean 组合定义的配置形式，用一种更加简单而可读的方式呈现出来。基于 Scheme 的 XML 由三部分构成，我们用一个示例说明：</p>
<pre><code>&lt;master-slave:load-balance-algorithm id=&quot;randomStrategy&quot;/&gt;
</code></pre>
<p>这段 XML 中，master-slave 是命名空间，从这个命名空间中可以明确地区分出所属的逻辑分类是用于实现读写分离；load-balance-algorithm 是一种元素，代表用于设置读写分离中的负载均衡算法；而 ID 就是负载均衡下的一个配置选项，它的值为随机策略 randomStrategy。</p>
<p>在 ShardingSphere 中，我们同样可以基于命名空间来实现完整的读写分离配置：</p>
<pre><code>&lt;beans
    ...
    http://shardingsphere.apache.org/schema/shardingsphere/masterslave
    http://shardingsphere.apache.org/schema/shardingsphere/masterslave/master-slave.xsd&quot;&gt; 
	&lt;bean id=&quot; dsmaster &quot; class=&quot; com.alibaba.druid.pool.DruidDataSource&quot; destroy-method=&quot;close&quot;&gt;
        &lt;property name=&quot;driverClassName&quot; value=&quot;com.mysql.jdbc.Driver&quot;/&gt;
        &lt;property name=&quot;url&quot; value=&quot;jdbc:mysql://localhost:3306/dsmaster&quot;/&gt;
        &lt;property name=&quot;username&quot; value=&quot;root&quot;/&gt;
        &lt;property name=&quot;password&quot; value=&quot;root&quot;/&gt;
    &lt;/bean&gt;

    &lt;bean id=&quot;dsslave0&quot; class=&quot;com.alibaba.druid.pool.DruidDataSource&quot; destroy-method=&quot;close&quot;&gt;
        &lt;property name=&quot;driverClassName&quot; value=&quot;com.mysql.jdbc.Driver&quot;/&gt;
        &lt;property name=&quot;url&quot; value=&quot;jdbc:mysql://localhost:3306/dsslave0&quot;/&gt;
        &lt;property name=&quot;username&quot; value=&quot;root&quot;/&gt;
        &lt;property name=&quot;password&quot; value=&quot;root&quot;/&gt;
    &lt;/bean&gt;

   &lt;bean id=&quot;dsslave1&quot; class=&quot;com.alibaba.druid.pool.DruidDataSource&quot; destroy-method=&quot;close&quot;&gt;
        &lt;property name=&quot;driverClassName&quot; value=&quot;com.mysql.jdbc.Driver&quot;/&gt;
        &lt;property name=&quot;url&quot; value=&quot;jdbc:mysql://localhost:3306/dsslave1&quot;/&gt;
        &lt;property name=&quot;username&quot; value=&quot;root&quot;/&gt;
        &lt;property name=&quot;password&quot; value=&quot;root&quot;/&gt;
    &lt;/bean&gt; 
    &lt;master-slave:load-balance-algorithm id=&quot;randomStrategy&quot; type=&quot;RANDOM&quot; /&gt;
    &lt;master-slave:data-source id=&quot;masterSlaveDataSource&quot; master-data-source-name=&quot;dsmaster&quot; slave-data-source-names=&quot;dsslave0, dsslave1&quot; strategy-ref=&quot;randomStrategy&quot; /&gt;

&lt;/beans&gt;
</code></pre>
<p>在这段代码中，我们在 Spring 中引入了 master-slave 这个新的命名空间，并完成了负载均衡算法和三个主从 DataSource 的设置。</p>
<h4>Spring Boot 配置</h4>
<p>Spring Boot 已经成为 Java 领域最流行的开发框架，提供了约定优于配置的设计理念。通常，开发人员可以把配置项放在 application.properties 文件中。同时，为了便于对配置信息进行管理和维护，Spring Boot 也提供了 profile 的概念，可以基于 profile 来灵活组织面对不同环境或应用场景的配置信息。在采用 profile 时，配置文件的命名方式有一定的约定：</p>
<pre><code>{application}-{profile}.properties
</code></pre>
<p>基于这种命名约定，如果我们根据面向的是传统的单库单表场景，还是主从架构的读写分离场景进行命名，就需要分别提供两个不同的 .properties 配置文件，如下面的代码所示：</p>
<pre><code>application-traditional.properties
application-master-slave.properties
</code></pre>
<p>这两个文件名中的 traditional 和 master-slave 就是具体的 profile，现在在 application.properties 文件中就可以使用 spring.profiles.active 配置项来设置当前所使用的 profile：</p>
<pre><code>#spring.profiles.active=traditional
spring.profiles.active=master-slave
</code></pre>
<p>基于 Spring Boot 的配置风格就是一组键值对，我们同样可以采用这种方式来实现前面介绍的读写分离配置：</p>
<pre><code>spring.shardingsphere.datasource.names=dsmaster,dsslave0,dsslave1 
spring.shardingsphere.datasource.dsmaster.type=com.alibaba.druid.pool.DruidDataSource
spring.shardingsphere.datasource.dsmaster.driver-class-name=com.mysql.jdbc.Driver
spring.shardingsphere.datasource.dsmaster.url=jdbc:mysql://localhost:3306/dsmaster
spring.shardingsphere.datasource.dsmaster.username=root
spring.shardingsphere.datasource.dsmaster.password=root 
spring.shardingsphere.datasource.dsslave0.type=com.alibaba.druid.pool.DruidDataSource
spring.shardingsphere.datasource.dsslave0.driver-class-name=com.mysql.jdbc.Driver
spring.shardingsphere.datasource.dsslave0.url=jdbc:mysql://localhost:3306/dsslave0
spring.shardingsphere.datasource.dsslave0.username=root
spring.shardingsphere.datasource.dsslave0.password=root 
spring.shardingsphere.datasource.dsslave1.type=com.alibaba.druid.pool.DruidDataSource
spring.shardingsphere.datasource.dsslave1.driver-class-name=com.mysql.jdbc.Driver
spring.shardingsphere.datasource.dsslave1.url=jdbc:mysql://localhost:3306/dsslave1
spring.shardingsphere.datasource.dsslave1.username=root
spring.shardingsphere.datasource.dsslave1.password=root 
spring.shardingsphere.masterslave.load-balance-algorithm-type=random
spring.shardingsphere.masterslave.name=health_ms
spring.shardingsphere.masterslave.master-data-source-name=dsmaster
spring.shardingsphere.masterslave.slave-data-source-names=dsslave0,dsslave1
</code></pre>
<p>通过这些不同的配置方式，开发人员可以基于自己擅长的或开发框架所要求的方式，灵活完成各项配置工作。在本课程中的后续内容中，我们会组合使用 Yaml 配置和 Spring Boot 配置这两种配置方式来介绍 ShardingSphere 的具体使用方式。</p>
<h3>ShardingSphere 的配置体系是如何实现的？</h3>
<p>尽管在日常开发过程中很少使用，但在前面介绍的四种配置方式中，Java 代码配置的实现方式最容易理解，我们可以通过各个配置类的调用关系来梳理 ShardingSphere 提供的配置功能。所以，为了深入理解配置体系的实现原理，我们还是选择从 ShardingRuleConfiguration 类进行切入。</p>
<h4>ShardingRuleConfiguration 配置体系</h4>
<p>对于 ShardingSphere 而言，配置体系的作用本质上就是用来初始化 DataSource 等 JDBC 对象。例如，ShardingDataSourceFactory 就是基于传入的数据源 Map、ShardingRuleConfiguration 以及 Properties 来创建一个 ShardingDataSource 对象：</p>
<pre><code>public final class ShardingDataSourceFactory {

    public static DataSource createDataSource(
            final Map&lt;String, DataSource&gt; dataSourceMap, final ShardingRuleConfiguration shardingRuleConfig, final Properties props) throws SQLException {
        return new ShardingDataSource(dataSourceMap, new ShardingRule(shardingRuleConfig, dataSourceMap.keySet()), props);
	} 
}
</code></pre>
<p>在 ShardingSphere 中，所有规则配置类都实现了一个顶层接口 RuleConfiguration。RuleConfiguration 是一个空接口，ShardingRuleConfiguration 就是这个接口的实现类之一，专门用来处理分片引擎的应用场景。下面这段代码就是 ShardingRuleConfiguration 类的实现过程：</p>
<pre><code>public final class ShardingRuleConfiguration implements RuleConfiguration {
    //表分片规则列表
    private Collection&lt;TableRuleConfiguration&gt; tableRuleConfigs = new LinkedList&lt;&gt;();
    //绑定表规则列表
    private Collection&lt;String&gt; bindingTableGroups = new LinkedList&lt;&gt;();
    //广播表规则列表
    private Collection&lt;String&gt; broadcastTables = new LinkedList&lt;&gt;();
    //默认数据源
    private String defaultDataSourceName;
    //默认分库策略
    private ShardingStrategyConfiguration defaultDatabaseShardingStrategyConfig;
    //默认分表策略
    private ShardingStrategyConfiguration defaultTableShardingStrategyConfig;
    //默认自增列值生成器
    private KeyGeneratorConfiguration defaultKeyGeneratorConfig;
    //读写分离规则
    private Collection&lt;MasterSlaveRuleConfiguration&gt; masterSlaveRuleConfigs = new LinkedList&lt;&gt;();
    //数据脱敏规则
    private EncryptRuleConfiguration encryptRuleConfig;
}
</code></pre>
<p>可以看到，ShardingRuleConfiguration 中包含的就是一系列的配置类定义，通过前面的内容介绍，我们已经明白了这些配置类的作用和使用方法。其中，核心的 TableRuleConfiguration 定义也比较简单，主要包含了逻辑表、真实数据节点以及分库策略和分表策略的定义：</p>
<pre><code>public final class TableRuleConfiguration {
    //逻辑表
    private final String logicTable;
    //真实数据节点
    private final String actualDataNodes;
    //分库策略
    private ShardingStrategyConfiguration databaseShardingStrategyConfig;
    //分表策略
    private ShardingStrategyConfiguration tableShardingStrategyConfig;
    //自增列生成器
    private KeyGeneratorConfiguration keyGeneratorConfig;

    public TableRuleConfiguration(final String logicTable) {
        this(logicTable, null);
    }

    public TableRuleConfiguration(final String logicTable, final String actualDataNodes) {
        Preconditions.checkArgument(!Strings.isNullOrEmpty(logicTable), &quot;LogicTable is required.&quot;);
        this.logicTable = logicTable;
        this.actualDataNodes = actualDataNodes;
    }
}
</code></pre>
<p>因为篇幅有限，我们不对其他配置类的定义做具体展开。事实上，无论采用哪种配置方式，所有的配置项都是在这些核心配置类的基础之上进行封装和转换。基于 Spring 命名空间和 Spring Boot 配置的使用方式比较常见，这两种方式的实现原理都依赖于 ShardingSphere 与这两个框架的集成方式，我会在后续课时中做详细展开。而 Yaml 配置是 ShardingSphere 非常推崇的一种使用方式，为此，ShardingSphere 在内部对 Yaml 配置的应用场景有专门的处理。今天，我们就来详细解析一下针对 Yaml 配置的完整实现方案。</p>
<h4>YamlShardingRuleConfiguration 配置体系</h4>
<p>在 ShardingSphere 源码的 sharding-core-common 工程中，存在一个包结构 org.apache.shardingsphere.core.yaml.config，在这个包结构下包含着所有与 Yaml 配置相关的实现类。</p>
<p>与 RuleConfiguration 一样，ShardingSphere 同样提供了一个空的 YamlConfiguration 接口。这个接口的实现类非常多，但我们发现其中包含了唯一的一个抽象类 YamlRootRuleConfiguration，显然，这个类是 Yaml 配置体系中的基础类。 在这个 YamlRootRuleConfiguration 中，包含着数据源 Map 和 Properties：</p>
<pre><code>public abstract class YamlRootRuleConfiguration implements YamlConfiguration {

    private Map&lt;String, DataSource&gt; dataSources = new HashMap&lt;&gt;();

    private Properties props = new Properties();
}
</code></pre>
<p>在上面这段代码中，我们发现少了 ShardingRuleConfiguration 的对应类，其实，这个类的定义在 YamlRootRuleConfiguration 的子类 YamlRootShardingConfiguration 中，它的类名 YamlShardingRuleConfiguration 就是在 ShardingRuleConfiguration 上加了一个 Yaml 前缀，如下面这段代码所示：</p>
<pre><code>public class YamlRootShardingConfiguration extends YamlRootRuleConfiguration {

    private YamlShardingRuleConfiguration shardingRule;
}
</code></pre>
<p>接下来，我们来到 YamlShardingRuleConfiguration 类，发现它所包含的变量与 ShardingRuleConfiguration 类中的变量存在一致对应关系，这些 Yaml 配置类都位于 org.apache.shardingsphere.core.yaml.config.sharding 包中：</p>
<pre><code>public class YamlShardingRuleConfiguration implements YamlConfiguration {

    private Map&lt;String, YamlTableRuleConfiguration&gt; tables = new LinkedHashMap&lt;&gt;(); 
    private Collection&lt;String&gt; bindingTables = new ArrayList&lt;&gt;(); 
    private Collection&lt;String&gt; broadcastTables = new ArrayList&lt;&gt;();
    private String defaultDataSourceName;
    private YamlShardingStrategyConfiguration defaultDatabaseStrategy;
    private YamlShardingStrategyConfiguration defaultTableStrategy;
    private YamlKeyGeneratorConfiguration defaultKeyGenerator; 
    private Map&lt;String, YamlMasterSlaveRuleConfiguration&gt; masterSlaveRules = new LinkedHashMap&lt;&gt;(); 
    private YamlEncryptRuleConfiguration encryptRule;
}
</code></pre>
<p>那么这个 YamlShardingRuleConfiguration 是怎么构建出来的呢？这就要来到 YamlShardingDataSourceFactory 工厂类，这个工厂类实际上是对 ShardingDataSourceFactory 类的进一步封装，下面这段代码就演示了这一过程：</p>
<pre><code>public final class YamlShardingDataSourceFactory {

    public static DataSource createDataSource(final File yamlFile) throws SQLException, IOException {
        YamlRootShardingConfiguration config = YamlEngine.unmarshal(yamlFile, YamlRootShardingConfiguration.class);
        return ShardingDataSourceFactory.createDataSource(config.getDataSources(), new ShardingRuleConfigurationYamlSwapper().swap(config.getShardingRule()), config.getProps());
	}
	…
}
</code></pre>
<p>可以看到 createDataSource 方法的输入参数是一个 File 对象，我们通过这个 File 对象构建出 YamlRootShardingConfiguration 对象，然后再通过 YamlRootShardingConfiguration 对象获取了 ShardingRuleConfiguration 对象，并交由 ShardingDataSourceFactory 完成目标 DataSource 的构建。这里的调用关系有点复杂，我们来梳理整个过程的类层结构，如下图所示：</p>
<p><img src="assets/Ciqc1F75rqaAGL8qAABR8QxogB0683.png" alt="image" /></p>
<p>显然，这里引入了两个新的工具类，YamlEngine 和 YamlSwapper。我们来看一下它们在整个流程中起到的作用。</p>
<h4>YamlEngine 和 YamlSwapper</h4>
<p>YamlEngine 的作用是将各种形式的输入内容转换成一个 Yaml 对象，这些输入形式包括 File、字符串、byte[] 等。YamlEngine 包含了一批 unmarshal/marshal 方法来完成数据的转换。以 File 输入为例，unmarshal 方法通过加载 FileInputStream 来完成 Yaml 对象的构建：</p>
<pre><code>    public static &lt;T extends YamlConfiguration&gt; T unmarshal(final File yamlFile, final Class&lt;T&gt; classType) throws IOException {
        try (
                FileInputStream fileInputStream = new FileInputStream(yamlFile);
                InputStreamReader inputStreamReader = new InputStreamReader(fileInputStream, &quot;UTF-8&quot;)
        ) {
            return new Yaml(new Constructor(classType)).loadAs(inputStreamReader, classType);
        }
    }
</code></pre>
<p>当在 unmarshal 方法中传入想要的 classType 时，我们就可以获取这个 classType 对应的实例。在 YamlShardingDataSourceFactory 中我们传入了 YamlRootShardingConfiguration 类型，这样我们就将得到一个 YamlRootShardingConfiguration 的类实例 YamlShardingRuleConfiguration。</p>
<p>在得到 YamlShardingRuleConfiguration 之后，下一步需要实现将 YamlShardingRuleConfiguration 转换为 ShardingRuleConfiguration。为了完成这种具有对应关系的类地转换，ShardingSphere 还专门提供了一批转换器类，ShardingRuleConfigurationYamlSwapper 就是其中之一。ShardingRuleConfigurationYamlSwapper 实现了 YamlSwapper 接口：</p>
<pre><code>public interface YamlSwapper&lt;Y extends YamlConfiguration, T&gt; {
    Y swap(T data);
    T swap(Y yamlConfiguration);
}
</code></pre>
<p>可以看到这里提供了一对方法完成两种数据结构之间的相互转换，ShardingRuleConfigurationYamlSwapper 中对这两个方法的实现过程也比较直接。以目标对象为 ShardingRuleConfiguration 的 swap 方法为例，代码结构基本上就是完成了 YamlShardingRuleConfiguration 与 ShardingRuleConfiguration 中对应字段的一对一转换：</p>
<pre><code>	@Override
    public ShardingRuleConfiguration swap(final YamlShardingRuleConfiguration yamlConfiguration) {
        ShardingRuleConfiguration result = new ShardingRuleConfiguration();
        for (Entry&lt;String, YamlTableRuleConfiguration&gt; entry : yamlConfiguration.getTables().entrySet()) {
            YamlTableRuleConfiguration tableRuleConfig = entry.getValue();
            tableRuleConfig.setLogicTable(entry.getKey());
            result.getTableRuleConfigs().add(tableRuleConfigurationYamlSwapper.swap(tableRuleConfig));
        }
        result.setDefaultDataSourceName(yamlConfiguration.getDefaultDataSourceName());
        result.getBindingTableGroups().addAll(yamlConfiguration.getBindingTables());
        result.getBroadcastTables().addAll(yamlConfiguration.getBroadcastTables());
        if (null != yamlConfiguration.getDefaultDatabaseStrategy()) {
            result.setDefaultDatabaseShardingStrategyConfig(shardingStrategyConfigurationYamlSwapper.swap(yamlConfiguration.getDefaultDatabaseStrategy()));
        }
        if (null != yamlConfiguration.getDefaultTableStrategy()) {
            result.setDefaultTableShardingStrategyConfig(shardingStrategyConfigurationYamlSwapper.swap(yamlConfiguration.getDefaultTableStrategy()));
        }
        if (null != yamlConfiguration.getDefaultKeyGenerator()) {
            result.setDefaultKeyGeneratorConfig(keyGeneratorConfigurationYamlSwapper.swap(yamlConfiguration.getDefaultKeyGenerator()));
        }
        Collection&lt;MasterSlaveRuleConfiguration&gt; masterSlaveRuleConfigs = new LinkedList&lt;&gt;();
        for (Entry&lt;String, YamlMasterSlaveRuleConfiguration&gt; entry : yamlConfiguration.getMasterSlaveRules().entrySet()) {
            YamlMasterSlaveRuleConfiguration each = entry.getValue();
            each.setName(entry.getKey());
            masterSlaveRuleConfigs.add(masterSlaveRuleConfigurationYamlSwapper.swap(entry.getValue()));
        }
        result.setMasterSlaveRuleConfigs(masterSlaveRuleConfigs);
        if (null != yamlConfiguration.getEncryptRule()) {
            result.setEncryptRuleConfig(encryptRuleConfigurationYamlSwapper.swap(yamlConfiguration.getEncryptRule()));
        }
        return result;
    }
</code></pre>
<p>这样，我们就从外部的 Yaml 文件中获取了一个 ShardingRuleConfiguration 对象，然后可以使用 ShardingDataSourceFactory 工厂类完成目标 DataSource 的创建过程。</p>
<h3>小结</h3>
<p>承接上一课时的内容，本课时我们对 ShardingSphere 中的配置体系进行了全面的介绍。事实上，在使用这个框架时，配置是开发人员最主要的工作内容。我们对 ShardingSphere 的核心配置项进行了梳理，然后给出了具体的四种配置方式，分别是 Java 代码配置、Yaml 配置、Spring 命名空间配置以及 Spring Boot 配置。最后，从实现原理上，我们也对 Yaml 配置这一特定的配置方式进行了深入的剖析。</p>
<p>这里给你留一道思考题：在 ShardingSphere中，配置体系相关的核心类之间存在什么样的关联关系？</p>
<p>从下一课时开始，我们就将基于 ShardingSphere 提供的配置体系，来逐步完成分库分表、读写分离以及分库分表+读写分离等操作的开发工作。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="04&#32;&#32;应用集成：在业务系统中使用&#32;ShardingSphere&#32;的方式有哪些？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/ShardingSphere%20%E6%A0%B8%E5%BF%83%E5%8E%9F%E7%90%86%E7%B2%BE%E8%AE%B2-%E5%AE%8C/06%20%20%E6%95%B0%E6%8D%AE%E5%88%86%E7%89%87%EF%BC%9A%E5%A6%82%E4%BD%95%E5%AE%9E%E7%8E%B0%E5%88%86%E5%BA%93%E3%80%81%E5%88%86%E8%A1%A8%E3%80%81%E5%88%86%E5%BA%93+%E5%88%86%E8%A1%A8%E4%BB%A5%E5%8F%8A%E5%BC%BA%E5%88%B6%E8%B7%AF%E7%94%B1%EF%BC%9F%EF%BC%88%E4%B8%8A%EF%BC%89.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434c1bb84a70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
