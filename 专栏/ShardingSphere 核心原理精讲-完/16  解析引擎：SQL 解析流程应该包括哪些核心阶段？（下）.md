<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>16  解析引擎：SQL 解析流程应该包括哪些核心阶段？（下）.md</title>
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

                    <a class="current-tab" href="16&#32;&#32;解析引擎：SQL&#32;解析流程应该包括哪些核心阶段？（下）.md">16  解析引擎：SQL 解析流程应该包括哪些核心阶段？（下）.md</a>
                    

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
                        <div><h1>16  解析引擎：SQL 解析流程应该包括哪些核心阶段？（下）</h1>
<p>我们知道整个 SQL 解析引擎可以分成三个阶段（如下图所示），上一课时我们主要介绍了 ShardingSphere 中 SQL 解析引擎的第一个阶段，那么今天我将承接上一课时，继续讲解 ShardingSphere 中 SQL 解析流程中剩余的两个阶段。</p>
<p><img src="assets/Ciqc1F8ry7-AWFaOAACKmUmdLPs289.png" alt="Drawing 0.png" /></p>
<h3>SQL 解析引擎的三大阶段</h3>
<p>在 SQL 解析引擎的第一阶段中，我们详细介绍了 ShardingSphere 生成 SQL 抽象语法树的过程，并引出了 SQLStatementRule 规则类。今天我们将基于这个规则类来分析如何提取 SQLSegment 以及如何填充 SQL 语句的实现机制。</p>
<h4>1.第二阶段：提取 SQL 片段</h4>
<p>要理解 SQLStatementRule，就需要先介绍 ParseRuleRegistry 类。从命名上看，该类就是一个规则注册表，保存着各种解析规则信息。ParseRuleRegistry 类中的核心变量包括如下所示的三个 Loader 类：</p>
<pre><code>	private final ExtractorRuleDefinitionEntityLoader extractorRuleLoader = new ExtractorRuleDefinitionEntityLoader(); 
     
    private final FillerRuleDefinitionEntityLoader fillerRuleLoader = new FillerRuleDefinitionEntityLoader(); 
     
    private final SQLStatementRuleDefinitionEntityLoader statementRuleLoader = new SQLStatementRuleDefinitionEntityLoader(); 
</code></pre>
<p>从命名上可以看到这三个 Loader 类分别处理对 SQLStatementRule、ExtractorRule 和 FillerRule 这三种规则定义的加载。</p>
<p>我们先来看 SQLStatementRule，它们的定义位于 sql-statement-rule-definition.xml 配置文件中。我们以 Mysql 为例，这个配置文件位于 shardingsphere-sql-parser-mysql 工程中的 META-INF/parsing-rule-definition/mysql 目录下。我们截取该配置文件中的部分配置信息作为演示，如下所示：</p>
<pre><code>&lt;sql-statement-rule-definition&gt; 
    &lt;sql-statement-rule context=&quot;select&quot; sql-statement-class=&quot;org.apache.shardingsphere.sql.parser.sql.statement.dml.SelectStatement&quot; extractor-rule-refs=&quot;tableReferences, columns, selectItems, where, predicate, groupBy, orderBy, limit, subqueryPredicate, lock&quot; /&gt; 
    &lt;sql-statement-rule context=&quot;insert&quot; sql-statement-class=&quot;org.apache.shardingsphere.sql.parser.sql.statement.dml.InsertStatement&quot; extractor-rule-refs=&quot;table, columns, insertColumns, insertValues, setAssignments, onDuplicateKeyColumns&quot; /&gt; 
    &lt;sql-statement-rule context=&quot;update&quot; sql-statement-class=&quot;org.apache.shardingsphere.sql.parser.sql.statement.dml.UpdateStatement&quot; extractor-rule-refs=&quot;tableReferences, columns, setAssignments, where, predicate&quot; /&gt; 
    &lt;sql-statement-rule context=&quot;delete&quot; sql-statement-class=&quot;org.apache.shardingsphere.sql.parser.sql.statement.dml.DeleteStatement&quot; extractor-rule-refs=&quot;tables, columns, where, predicate&quot; /&gt; 
… 
&lt;/sql-statement-rule-definition&gt; 
</code></pre>
<p>基于 ParseRuleRegistry 类进行规则获取和处理过程，涉及一大批实体对象以及用于解析 XML 配置文件的 JAXB 工具类的定义，内容虽多但并不复杂。核心类之间的关系如下图所示：</p>
<p><img src="assets/Ciqc1F8ry9CAPtDdAACEYYKrCTU070.png" alt="Drawing 2.png" /></p>
<p>ParseRuleRegistry 类层结构图</p>
<p>当获取规则之后，对于具体某种数据库类型的每条 SQL 而言，都会有一个 SQLStatementRule 对象。我们注意到每个 SQLStatementRule 都定义了一个“context”以及一个“sql-statement-class”。</p>
<p>这里的 context 实际上就是通过 SQL 解析所生成的抽象语法树 SQLAST 中的 ParserRuleContext，包括 CreateTableContext、SelectContext 等各种 StatementContext。而针对每一种 context，都有专门的一个 SQLStatement 对象与之对应，那么这个 SQLStatement 究竟长什么样呢？我们来看一下。</p>
<pre><code>public interface SQLStatement { 
     
    //获取参数个数 
    int getParametersCount(); 
     
    //获取所有SQLSegment 
    Collection&lt;SQLSegment&gt; getAllSQLSegments(); 
     
    //根据类型获取一个SQLSegment 
    &lt;T extends SQLSegment&gt; Optional&lt;T&gt; findSQLSegment(Class&lt;T&gt; sqlSegmentType); 
     
    //根据类型获取一组SQLSegment 
    &lt;T extends SQLSegment&gt; Collection&lt;T&gt; findSQLSegments(Class&lt;T&gt; sqlSegmentType); 
} 
</code></pre>
<p>你可以看到，作为解析引擎最终产物的 SQLStatement ，实际上封装的是对 SQL 片段对象 SQLSegment 的获取操作。显然，对于每一个 ParserRuleContext 而言，我们最终就是构建了一个包含一组 SQLSegment 的 SQLStatement 对象，而这些 SQLSegment 的构建过程就是所谓的提取 SQLSegment 的过程。我们在配置文件中也明确看到了 SQLStatementRule 中对各种提取规则对象 ExtractorRule 的引用。</p>
<p>在 ShardingSphere 中内置了一大批通用的 SQLSegment，包括查询选择项（SelectItems）、表信息（Table）、排序信息（OrderBy）、分组信息（GroupBy）以及分页信息（Limit）等。这些通用 SQLSegment 都有对应的 SQLSegmentExtractor，我们可以直接在 SQLStatementRule 中进行使用。</p>
<p>另一方面，考虑到 SQL 方言的差异性，ShardingSphere 同样提供了针对各种数据库的 SQLSegment 的提取器定义。以 Mysql 为例，在其代码工程的 META-INF/parsing-rule-definition/mysql 目录下，存在一个 extractor-rule-definition.xml 配置文件，专门用来定义针对 Mysql 的各种 SQLSegmentExtractor，部分定义如下所示，作为一款适用于多数据库的中间件，这也是 ShardingSphere 应对 SQL 方言的实现机制之一。</p>
<pre><code>&lt;extractor-rule-definition&gt; 
    &lt;extractor-rule id=&quot;addColumnDefinition&quot; extractor-class=&quot;org.apache.shardingsphere.sql.parser.core.extractor.ddl.MySQLAddColumnDefinitionExtractor&quot; /&gt; 
    &lt;extractor-rule id=&quot;modifyColumnDefinition&quot; extractor-class=&quot;org.apache.shardingsphere.sql.parser.core.extractor.ddl.MySQLModifyColumnDefinitionExtractor&quot; /&gt; 
    … 
&lt;/extractor-rule-definition&gt; 
</code></pre>
<p>现在，假设有这样一句 SQL：</p>
<pre><code>SELECT task_id, task_name FROM health_task WHERE user_id = 'user1' AND record_id = 2  
</code></pre>
<p>通过解析，我们获取了如下所示的抽象语法树：</p>
<p><img src="assets/Ciqc1F8ry_WAEwAzAACKQ3CnEFw961.png" alt="Drawing 4.png" /></p>
<p>抽象语法树示意图</p>
<p>我们发现，对于上述抽象语法树中的某些节点（如 SELECT、FROM 和 WHERE）没有子节点，而对于如 FIELDS、TABLES 和 CONDITIONS 节点而言，本身也是一个树状结构。显然，这两种节点的提取规则应该是不一样的。</p>
<p>因此，ShardingSphere 提供了两种 SQLSegmentExtractor，一种是针对单节点的 OptionalSQLSegmentExtractor；另一种是针对树状节点的 CollectionSQLSegmentExtractor。由于篇幅因素，这里以 TableExtractor 为例，展示如何提取 TableSegment 的过程，TableExtractor 的实现方法如下所示：</p>
<pre><code>public final class TableExtractor implements OptionalSQLSegmentExtractor { 
     
    @Override 
    public Optional&lt;TableSegment&gt; extract(final ParserRuleContext ancestorNode, final Map&lt;ParserRuleContext, Integer&gt; parameterMarkerIndexes) { 
        //从Context中获取TableName节点 
     Optional&lt;ParserRuleContext&gt; tableNameNode = ExtractorUtils.findFirstChildNode(ancestorNode, RuleName.TABLE_NAME); 
        if (!tableNameNode.isPresent()) { 
            return Optional.absent(); 
        }         
        //根据TableName节点构建TableSegment 
        TableSegment result = getTableSegment(tableNameNode.get()); 
        //设置表的别名 
        setAlias(tableNameNode.get(), result); 
        return Optional.of(result); 
    } 
     
    private TableSegment getTableSegment(final ParserRuleContext tableNode) { 
     //从Context中获取Name节点       
        ParserRuleContext nameNode = ExtractorUtils.getFirstChildNode(tableNode, RuleName.NAME); 
        //根据Name节点获取节点的起止位置以及节点内容 
        TableSegment result = new TableSegment(nameNode.getStart().getStartIndex(), nameNode.getStop().getStopIndex(), nameNode.getText()); 
        //从Context中获取表的Owner节点，如果有的话就设置Owner 
        Optional&lt;ParserRuleContext&gt; ownerNode = ExtractorUtils.findFirstChildNodeNoneRecursive(tableNode, RuleName.OWNER); 
        if (ownerNode.isPresent()) { 
            result.setOwner(new SchemaSegment(ownerNode.get().getStart().getStartIndex(), ownerNode.get().getStop().getStopIndex(), ownerNode.get().getText())); 
        } 
        return result; 
    } 
     
    private void setAlias(final ParserRuleContext tableNameNode, final TableSegment tableSegment) { 
     //从Context中获取Alias节点，如果有的话就设置别名 
     Optional&lt;ParserRuleContext&gt; aliasNode = ExtractorUtils.findFirstChildNode(tableNameNode.getParent(), RuleName.ALIAS); 
        if (aliasNode.isPresent()) { 
            tableSegment.setAlias(aliasNode.get().getText()); 
        } 
    } 
} 
</code></pre>
<p>显然，语法树中的 Table 是一种单节点，所以 TableExtractor 继承自 OptionalSQLSegmentExtractor。对于 TableExtractor 而言，整个解析过程就是从 ParserRuleContext 中获取与表定义相关的各种节点，然后通过节点的起止位置以及节点内容来构建 TableSegment 对象。TableSegment 实现了 SQLSegment，其核心变量的定义也比较明确，如下所示：</p>
<pre><code>public final class TableSegment implements SQLSegment, TableAvailable, OwnerAvailable&lt;SchemaSegment&gt;, AliasAvailable { 
     
    private final int startIndex;     
    private final int stopIndex;   
    private final String name;  
    private final QuoteCharacter quoteCharacter; 
    private SchemaSegment owner;  
	private String alias; 
       … 
} 
</code></pre>
<p>现在，基于以上关于提取器以及提取操作的相关概念的理解，我们来看一下 SQLSegment 提取引擎 SQLSegmentsExtractorEngine 的实现，如下所示：</p>
<pre><code>public final class SQLSegmentsExtractorEngine { 
     
    //用来提取SQLAST语法树中的SQL片段 
    public Collection&lt;SQLSegment&gt; extract(final SQLAST ast) { 
        Collection&lt;SQLSegment&gt; result = new LinkedList&lt;&gt;(); 
         
        //遍历提取器，从Context中提取对应类型的SQLSegment，比如TableSegment         
        for (SQLSegmentExtractor each : ast.getSqlStatementRule().getExtractors()) {            
            //单节点的场景，直接提取单一节点下的内容 
            if (each instanceof OptionalSQLSegmentExtractor) { 
                Optional&lt;? extends SQLSegment&gt; sqlSegment = ((OptionalSQLSegmentExtractor) each).extract(ast.getParserRuleContext(), ast.getParameterMarkerIndexes()); 
                if (sqlSegment.isPresent()) { 
                    result.add(sqlSegment.get()); 
                } 
                 
            树状节点的场景，遍历提取节点下的所有子节点// 
            } else if (each instanceof CollectionSQLSegmentExtractor) { 
                result.addAll(((CollectionSQLSegmentExtractor) each).extract(ast.getParserRuleContext(), ast.getParameterMarkerIndexes())); 
            } 
        } 
        return result; 
    } 
} 
</code></pre>
<p>显然，SQLSegmentsExtractorEngine 的作用就是针对某一条 SQL，遍历 SQLStatementRule 中所配置的提取器，然后从 Context 中提取对应类型的 SQLSegment，并最终存放在一个集合对象中进行返回。</p>
<h4>2.第三阶段：填充 SQL 语句</h4>
<p>完成所有 SQLSegment 的提取之后，我们就来到了解析引擎的最后一个阶段，即填充 SQLStatement。所谓的<strong>填充过程</strong>，就是通过填充器 SQLSegmentFiller 为 SQLStatement 注入具体 SQLSegment 的过程。这点从 SQLSegmentFiller 接口定义中的各个参数就可以得到明确，如下所示：</p>
<pre><code>public interface SQLSegmentFiller&lt;T extends SQLSegment&gt; { 
     
    void fill(T sqlSegment, SQLStatement sqlStatement); 
} 
</code></pre>
<p>那么问题就来了，我们如何正确把握 SQLSegmentFiller、SQLSegment 和 SQLStatement 这三者之间的处理关系呢？我们先根据某个 SQLSegment 找到对应的 SQLSegmentFiller，这部分关系在 ShardingSphere 中同样是维护在一个 filler-rule-definition.xml 配置文件中，截取部分配置项如下所示：</p>
<pre><code>&lt;filler-rule-definition&gt; 
    &lt;filler-rule sql-segment-class=&quot;org.apache.shardingsphere.sql.parser.sql.segment.generic.TableSegment&quot; filler-class=&quot;org.apache.shardingsphere.sql.parser.core.filler.impl.TableFiller&quot; /&gt; 
    &lt;filler-rule sql-segment-class=&quot;org.apache.shardingsphere.sql.parser.sql.segment.generic.SchemaSegment&quot; filler-class=&quot;org.apache.shardingsphere.sql.parser.core.filler.impl.dal.SchemaFiller&quot; /&gt; 
	… 
&lt;/filler-rule-definition&gt; 
</code></pre>
<p>显然，这里保存着 SQLSegment 与 SQLSegmentFiller 之间的对应关系。当然，对于不同的 SQL 方言，也同样可以维护自身的 filler-rule-definition.xml 文件。</p>
<p>我们还是以与 TableSegment 对应的 TableFiller 为例，来分析一个 SQLSegmentFiller 的具体实现方法，TableFiller 类如下所示：</p>
<pre><code>public final class TableFiller implements SQLSegmentFiller&lt;TableSegment&gt; { 
     
    @Override 
    public void fill(final TableSegment sqlSegment, final SQLStatement sqlStatement) { 
        if (sqlStatement instanceof TableSegmentAvailable) { 
            ((TableSegmentAvailable) sqlStatement).setTable(sqlSegment); 
        } else if (sqlStatement instanceof TableSegmentsAvailable) { 
            ((TableSegmentsAvailable) sqlStatement).getTables().add(sqlSegment); 
        } 
    } 
} 
</code></pre>
<p>这段代码在实现上采用了回调机制来完成对象的注入。在 ShardingSphere 中，基于回调的处理方式也非常普遍。本质上，回调解决了因为类与类之间的相互调用而造成的循环依赖问题，回调的实现策略通常采用了如下所示的类层结构：</p>
<p><img src="assets/Ciqc1F8rzBeAL-gtAAAtxVTlOkM440.png" alt="Drawing 6.png" /></p>
<p>回调机制示意图</p>
<p>TableFiller 中所依赖的 TableSegmentAvailable 和 TableSegmentsAvailable 接口就类似于上图中的 Callback 接口，具体的 SQLStatement 就是 Callback 的实现类，而 TableFiller 则是 Callback 的调用者。以 TableFiller 为例，我们注意到，如果对应的 SQLStatement 实现了这两个接口中的任意一个，那么就可以通过 TableFiller 注入对应的 TableSegment，从而完成 SQLSegment 的填充。</p>
<p>这里以 TableSegmentAvailable 接口为例，它有一组实现类，如下所示：</p>
<p><img src="assets/CgqCHl8rzC2ADPHvAAAxxRKUUYw921.png" alt="Drawing 8.png" /></p>
<p>TableSegmentAvailable实现类</p>
<p>以上图中的 CreateTableStatement 为例，该类同时实现了 TableSegmentAvailable 和 IndexSegmentsAvailable 这两个回调接口，所以就可以同时操作 TableSegment 和 IndexSegment 这两个 SQLSegment。CreateTableStatement 类的实现如下所示：</p>
<pre><code>public final class CreateTableStatement extends DDLStatement implements TableSegmentAvailable, IndexSegmentsAvailable { 
     
    private TableSegment table; 
     
    private final Collection&lt;ColumnDefinitionSegment&gt; columnDefinitions = new LinkedList&lt;&gt;(); 
     
    private final Collection&lt;IndexSegment&gt; indexes = new LinkedList&lt;&gt;(); 
} 
</code></pre>
<p>至此，我们通过一个示例解释了与填充操作相关的各个类之间的协作关系，如下所示的类图展示了这种协作关系的整体结构。</p>
<p><img src="assets/CgqCHl8rzDqAVtDCAAB-8xyeFnI893.png" alt="Drawing 9.png" /></p>
<p>SQLStatement类层结构图</p>
<p>有了上图的基础，我们理解填充引擎 SQLStatementFillerEngine 就显得比较简单了，SQLStatementFillerEngine 类的实现如下所示：</p>
<pre><code>public final class SQLStatementFillerEngine { 
     
    private final ParseRuleRegistry parseRuleRegistry;     
    private final String databaseTypeName; 
    
    @SuppressWarnings(&quot;unchecked&quot;) 
    @SneakyThrows 
    public SQLStatement fill(final Collection&lt;SQLSegment&gt; sqlSegments, final int parameterMarkerCount, final SQLStatementRule rule) { 
     //从SQLStatementRule中获取SQLStatement实例，如CreateTableStatement 
     SQLStatement result = rule.getSqlStatementClass().newInstance(); 
        //通过断言对SQLStatement的合法性进行校验 
     Preconditions.checkArgument(result instanceof AbstractSQLStatement, &quot;%s must extends AbstractSQLStatement&quot;, result.getClass().getName()); 
         
        //设置参数个数 
        ((AbstractSQLStatement) result).setParametersCount(parameterMarkerCount); 
       
        //添加所有的SQLSegment到SQLStatement中 
        result.getAllSQLSegments().addAll(sqlSegments); 
         
        //遍历填充对应类型的SQLSegment 
        for (SQLSegment each : sqlSegments) { 
         //根据数据库类型和SQLSegment找到对应的SQLSegmentFiller，并为SQLStatement填充SQLSegment 
            //如通过TableSegment找到获取TableFiller，然后通过TableFiller为CreateTableStatement填充TableSegment 
         Optional&lt;SQLSegmentFiller&gt; filler = parseRuleRegistry.findSQLSegmentFiller(databaseTypeName, each.getClass()); 
            if (filler.isPresent()) {                
              //利用SQLSegmentFiller来填充SQLStatement中的SQLSegment 
                filler.get().fill(each, result); 
            } 
        } 
        return result; 
	}  
} 
</code></pre>
<p>我们对 SQLStatementFillerEngine 中的核心代码都添加了注释，注意到这里通过数据库类型以及 SQLSegment 的类型，从规则注册表 ParseRuleRegistry 中获取了对应的 SQLSegmentFiller 并完成对 SQLStatement 的填充操作。</p>
<p>至此，ShardingSphere 中 SQL 解析引擎的三大阶段介绍完毕。我们已经获取了目标 SQLStatement，为进行后续的路由等操作提供了基础。</p>
<h3>从源码解析到日常开发</h3>
<p>通过对框架源代码的学习，一方面可以帮忙我们更好地理解该框架核心功能背后的实现原理；另一方面，我们也可以吸收这些优秀框架的设计思想和实现方法，从而更好地指导日常开发工作。在本文中，我们同样总结了一组设计和实现上的技巧。</p>
<h4>1.设计模式的应用方式</h4>
<p>在本文中，我们主要涉及了两种设计模式的应用场景，一种是工厂模式，另一种是外观模式。</p>
<p><strong>工厂模式</strong>的应用比较简单，作用也比较直接。例如，SQLParseEngineFactory 工厂类用于创建 SQLParseEngine，而 SQLParserFactory 工厂类用于创建 SQLParser。</p>
<p>相比工厂模式，<strong>外观类</strong>通常比较难识别和把握，因此，我们也花了一定篇幅介绍了 SQL 解析引擎中的外观类 SQLParseKernel，以及与 SQLParseEngine 之间的委托关系。</p>
<h4>2.缓存的实现方式</h4>
<p>缓存在 ShardingSphere 中应用非常广泛，其实现方式也比较多样，在本文中，我们就接触到了两种缓存的实现方式。</p>
<p>第一种是通过 ConcurrentHashMap 类来保存 SQLParseEngine 的实例，使用上比较简单。</p>
<p>另一种则基于 Guava 框架中的 Cache 类构建了一个 SQLParseResultCache 来保存 SQLStatement 对象。Guava 中的 Cache 类初始化方法如下所示，我们可以通过 put 和 getIfPresent 等方法对缓存进行操作：</p>
<pre><code>Cache&lt;String, SQLStatement&gt; cache = CacheBuilder.newBuilder().softValues().initialCapacity(2000).maximumSize(65535).build();     
</code></pre>
<h4>3.配置信息的两级管理机制</h4>
<p>在 ShardingSphere 中，关于各种提取规则和填充规则的定义都放在了 XML 配置文件中，并采用了配置信息的两级管理机制。这种<strong>两级管理机制</strong>的设计思想在于，系统在提供了对各种通用规则默认实现的同时，也能够集成来自各种 SQL 方言的定制化规则，从而形成一套具有较高灵活性以及可扩展性的规则管理体系。</p>
<h4>4.回调机制</h4>
<p>所谓<strong>回调</strong>，本质上就是一种<strong>双向调用模式</strong>，也就是说，被调用方在被调用的同时也会调用对方。在实现上，我们可以提取一个用于业务接口作为一种 Callback 接口，然后让具体的业务对象去实现这个接口。这样，当外部对象依赖于这个业务场景时，只需要依赖这个 Callback 接口，而不需要关心这个接口的具体实现类。</p>
<p>这在软件设计和实现过程中是一种常见的消除业务对象和外部对象之间循环依赖的处理方式。ShardingSphere 中大量采用了这种实现方式来确保代码的可维护性，这非常值得我们学习。</p>
<h3>小结</h3>
<p>作为 ShardingSphere 分片引擎的第一个核心组件，解析引擎的目的在于生成 SQLStatement 目标对象。而整个解析引擎分成三大阶段，即生成 SQL 抽象语法树、提取 SQL 片段以及使用这些片段来填充 SQL 语句。本文对解析引擎的整体结构以及这三个阶段进行了详细的讨论。</p>
<p>最后给你留一道思考题：简要介绍 ShardingSphere 中 SQL 解析的各个阶段的输入和产出？欢迎你在留言区与大家讨论，我将一一点评解答。</p>
<p>现在，我们已经获取了 SQLStatement，接下来就可以用来执行 SQL 路由操作，这就是下一课时内容。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="15&#32;&#32;解析引擎：SQL&#32;解析流程应该包括哪些核心阶段？（上）.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="17&#32;&#32;路由引擎：如何理解分片路由核心类&#32;ShardingRouter&#32;的运作机制？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434c64480770ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
