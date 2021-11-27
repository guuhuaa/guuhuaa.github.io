<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>23  执行引擎：如何把握 ShardingSphere 中的 Executor 执行模型？（下）.md</title>
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

                    <a class="current-tab" href="23&#32;&#32;执行引擎：如何把握&#32;ShardingSphere&#32;中的&#32;Executor&#32;执行模型？（下）.md">23  执行引擎：如何把握 ShardingSphere 中的 Executor 执行模型？（下）.md</a>
                    

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
                        <div><h1>23  执行引擎：如何把握 ShardingSphere 中的 Executor 执行模型？（下）</h1>
<p>在上一课时，我们已经对 ShardingSphere 执行引擎中关于底层的 SQLExecuteTemplate，以及上层的 StatementExecutor 和 PreparedStatementExecutor 对象进行了全面介绍。</p>
<p>今天，我们在此基础上更上一层，重点关注 ShardingStatement 和 ShardingPreparedStatement 对象，这两个对象分别是 StatementExecutor 和 PreparedStatementExecutor 的使用者。</p>
<h3>ShardingStatement</h3>
<p>我们先来看 ShardingStatement 类，该类中的变量在前面的内容中都已经有过介绍：</p>
<pre><code>private final ShardingConnection connection;
private final StatementExecutor statementExecutor;
private boolean returnGeneratedKeys;
private SQLRouteResult sqlRouteResult;
private ResultSet currentResultSet;
</code></pre>
<p>ShardingStatement 类的构造函数同样不是很复杂，我们发现 StatementExecutor 就是在这个构造函数中完成了其创建过程：</p>
<pre><code>public ShardingStatement(final ShardingConnection connection, final int resultSetType, final int resultSetConcurrency, final int resultSetHoldability) {
    super(Statement.class);
    this.connection = connection;
    //创建 StatementExecutor
    statementExecutor = new StatementExecutor(resultSetType, resultSetConcurrency, resultSetHoldability, connection);
}
</code></pre>
<p>在继续介绍 ShardingStatement 之前，我们先梳理一下与它相关的类层结构。我们在 <strong>“06 | 规范兼容：JDBC 规范与 ShardingSphere 是什么关系？”</strong> 中的 ShardingConnection 提到，ShardingSphere 通过适配器模式包装了自己的实现类，除了已经介绍的 ShardingConnection 类之外，还包含今天要介绍的 ShardingStatement 和 ShardingPreparedStament。</p>
<p>根据这一点，我们可以想象 ShardingStatement 应该具备与 ShardingConnection 类似的类层结构：</p>
<p><img src="assets/CgqCHl9MzLGAdeNfAACM0dnojxQ073.png" alt="Drawing 0.png" /></p>
<p>然后我们来到上图中 AbstractStatementAdapter 类，这里的很多方法的风格都与 ShardingConnection 的父类 AbstractConnectionAdapter 一致，例如如下所示的 setPoolable 方法：</p>
<pre><code>public final void setPoolable(final boolean poolable) throws SQLException {
    this.poolable = poolable;
    recordMethodInvocation(targetClass, &quot;setPoolable&quot;, new Class[] {boolean.class}, new Object[] {poolable});
    forceExecuteTemplate.execute((Collection) getRoutedStatements(), new ForceExecuteCallback&lt;Statement&gt;() {

        @Override
        public void execute(final Statement statement) throws SQLException {
            statement.setPoolable(poolable);
        }
    });
</code></pre>
<blockquote>
<p>这里涉及的 recordMethodInvocation 方法、ForceExecuteTemplate，以及 ForceExecuteCallback 我们都已经在“03 | 规范兼容：JDBC 规范与 ShardingSphere 是什么关系？”中进行了介绍，这里不再展开。</p>
</blockquote>
<p>同样，AbstractStatementAdapter 的父类 AbstractUnsupportedOperationStatement 的作用也与 AbstractUnsupportedOperationConnection 的作用完全一致。</p>
<p>了解了 ShardingStatement 的类层结构之后，我们来看它的核心方法，首当其冲的还是它的 executeQuery 方法：</p>
<pre><code>@Override
public ResultSet executeQuery(final String sql) throws SQLException {
    if (Strings.isNullOrEmpty(sql)) {
        throw new SQLException(SQLExceptionConstant.SQL_STRING_NULL_OR_EMPTY);
    }
    ResultSet result;
    try {
         //清除 StatementExecutor 中的相关变量
        clearPrevious();
        //执行路由引擎，获取路由结果
        shard(sql);
        //初始化 StatementExecutor
        initStatementExecutor();
        //调用归并引擎
        MergeEngine mergeEngine = MergeEngineFactory.newInstance(connection.getRuntimeContext().getDatabaseType(), connection.getRuntimeContext().getRule(), sqlRouteResult, connection.getRuntimeContext().getMetaData().getRelationMetas(), statementExecutor.executeQuery());
        //获取归并结果
        result = getResultSet(mergeEngine);
    } finally {
        currentResultSet = null;
    }
    currentResultSet = result;
    return result;
}
</code></pre>
<p>这个方法中有几个子方法值得具体展开一下，首先是 shard 方法：</p>
<pre><code>private void shard(final String sql) {
    //从 Connection 中获取 ShardingRuntimeContext 上下文
    ShardingRuntimeContext runtimeContext = connection.getRuntimeContext();
    //创建 SimpleQueryShardingEngine
    SimpleQueryShardingEngine shardingEngine = new SimpleQueryShardingEngine(runtimeContext.getRule(), runtimeContext.getProps(), runtimeContext.getMetaData(), runtimeContext.getParseEngine());
    //执行分片路由并获取路由结果
    sqlRouteResult = shardingEngine.shard(sql, Collections.emptyList());
}
</code></pre>
<p>这段代码就是路由引擎的入口，我们创建了 SimpleQueryShardingEngine，并调用它的 shard 方法获取路由结果对象 SQLRouteResult。</p>
<p>然后我们来看 initStatementExecutor 方法，如下所示：</p>
<pre><code>private void initStatementExecutor() throws SQLException {
    statementExecutor.init(sqlRouteResult);
    replayMethodForStatements();
}
</code></pre>
<p>这里通过路由结果对象 SQLRouteResult 对 statementExecutor 进行了初始化，然后执行了一个 replayMethodForStatements 方法：</p>
<pre><code>private void replayMethodForStatements() {
    for (Statement each : statementExecutor.getStatements()) {
        replayMethodsInvocation(each);
    }
}
</code></pre>
<p>该方法实际上就是调用了基于反射的 replayMethodsInvocation 方法，然后这个replayMethodsInvocation 方法会针对 statementExecutor 中所有 Statement的 SQL 操作执行目标方法。</p>
<p>最后，我们通过执行 statementExecutor.executeQuery() 方法获取 SQL 执行的结果，并用这个结果来创建<strong>归并引擎 MergeEngine</strong>，并通过归并引擎 MergeEngine 获取最终的执行结果。</p>
<blockquote>
<p><strong>归并引擎</strong>是 ShardingSphere 中与 SQL 解析引擎、路由引擎以及执行引擎并列的一个引擎，我们在下一课时中就会开始介绍这块内容，这里先不做具体展开。</p>
</blockquote>
<p>以 ShardingStatement 中的其中一个 executeUpdate 方法为例，可以看到它的执行流程也与前面的 executeQuery 方法非常类似：</p>
<pre><code>@Override
public int executeUpdate(final String sql) throws SQLException {
    try {
         //清除 StatementExecutor 中的相关变量
        clearPrevious();
        //执行路由引擎，获取路由结果
        shard(sql);
        //初始化 StatementExecutor
        initStatementExecutor();
        return statementExecutor.executeUpdate();
    } finally {
        currentResultSet = null;
    }
}
</code></pre>
<p>当然，对于 Update 操作而言，不需要通过归并引擎做结果的归并。</p>
<h3>ShardingPreparedStatement</h3>
<p>我们接着来看 ShardingPreparedStatement 类，这个类的变量也基本都是前面介绍过的对象：</p>
<pre><code>private final ShardingConnection connection;
private final String sql;
private final PreparedQueryShardingEngine shardingEngine;
private final PreparedStatementExecutor preparedStatementExecutor;
private final BatchPreparedStatementExecutor batchPreparedStatementExecutor;
private SQLRouteResult sqlRouteResult;
private ResultSet currentResultSet;
</code></pre>
<p>这里的 ShardingEngine、PreparedStatementExecutor 和 BatchPreparedStatementExecutor 对象的创建过程都发生在 ShardingPreparedStatement 的构造函数中。</p>
<p>然后我们来看它的代表性方法 ExecuteQuery，如下所示：</p>
<pre><code>@Override
public ResultSet executeQuery() throws SQLException {
    ResultSet result;
    try {
        clearPrevious();
        shard();
        initPreparedStatementExecutor();
        MergeEngine mergeEngine = MergeEngineFactory.newInstance(connection.getRuntimeContext().getDatabaseType(), connection.getRuntimeContext().getRule(), sqlRouteResult, connection.getRuntimeContext().getMetaData().getRelationMetas(), preparedStatementExecutor.executeQuery());
        result = getResultSet(mergeEngine);
    } finally {
        clearBatch();
    }
    currentResultSet = result;
    return result;
}
</code></pre>
<p>这里我们没加注释，但也应该理解这一方法的执行流程，因为该方法的风格与 ShardingStatement 中的同名方法非常一致。</p>
<p>关于 ShardingPreparedStatement 就没有太多可以介绍的内容了，我们接着来看它的父类<strong>AbstractShardingPreparedStatementAdapter 类</strong>，看到该类持有一个 SetParameterMethodInvocation 的列表，以及一个参数列表：</p>
<pre><code>private final List&lt;SetParameterMethodInvocation&gt; setParameterMethodInvocations = new LinkedList&lt;&gt;();
private final List&lt;Object&gt; parameters = new ArrayList&lt;&gt;();
</code></pre>
<p>这里的 SetParameterMethodInvocation 类直接集成了介绍 ShardingConnection 时提到的 JdbcMethodInvocation 类：</p>
<pre><code>public final class SetParameterMethodInvocation extends JdbcMethodInvocation {

    @Getter
    private final int index;

    @Getter
    private final Object value;

    public SetParameterMethodInvocation(final Method method, final Object[] arguments, final Object value) {
        super(method, arguments);
        this.index = (int) arguments[0];
        this.value = value;
    }

    public void changeValueArgument(final Object value) {
        getArguments()[1] = value;
    }
}
</code></pre>
<p>对于 ShardingPreparedStatement 而言，这个类的作用是在 JdbcMethodInvocation 中所保存的方法和参数的基础上，添加了 SQL 执行过程中所需要的参数信息。</p>
<p>所以它的 replaySetParameter 方法就变成了如下的风格：</p>
<pre><code>protected final void replaySetParameter(final PreparedStatement preparedStatement, final List&lt;Object&gt; parameters) {
    setParameterMethodInvocations.clear();
   //添加参数信息
    addParameters(parameters);
    for (SetParameterMethodInvocation each : setParameterMethodInvocations) {
        each.invoke(preparedStatement);
    }
}
</code></pre>
<p>关于 AbstractShardingPreparedStatementAdapter 还需要注意的是它的<strong>类层结构</strong>，如下图所示，可以看到 AbstractShardingPreparedStatementAdapter 继承了 AbstractUnsupportedOperationPreparedStatement 类；而 AbstractUnsupportedOperationPreparedStatement 却又继承了 AbstractStatementAdapter 类并实现了 PreparedStatement：</p>
<p><img src="assets/Ciqc1F9MzNeACiagAACzQd-8eig186.png" alt="Drawing 2.png" /></p>
<p>形成这种类层结构的原因在于，PreparedStatement 本来就是在 Statement 的基础上添加了各种参数设置功能，换句话说，Statement 的功能 PreparedStatement 都应该有。</p>
<p>所以一方面 AbstractStatementAdapter 提供了所有 Statement 的功能；另一方面，AbstractShardingPreparedStatementAdapter 首先把 AbstractStatementAdapter 所有的功能继承过来，但它自身可能有一些无法实现的关于 PreparedStatement 的功能，所以同样提供了 AbstractUnsupportedOperationPreparedStatement 类，并被最终的 AbstractShardingPreparedStatementAdapter 适配器类所继承。</p>
<p>这样就形成了如上图所示的复杂类层结构。</p>
<h3>ShardingConnection</h3>
<p>介绍完 ShardingStatement 和 ShardingPreparedStatement 之后，我们来关注使用它们的具体应用场景，这也是 ShardingSphere 执行引擎的最后一部分内容。</p>
<p>通过查看调用关系，我们发现创建这两个类的入口都在 ShardingConnection 类中，该类包含了用于创建 ShardingStatement 的 createStatement 方法和用于创建 ShardingPreparedStatement 的 prepareStatement 方法，以及它们的各种重载方法：</p>
<pre><code>@Override
public Statement createStatement(final int resultSetType, final int resultSetConcurrency, final int resultSetHoldability) {
    return new ShardingStatement(this, resultSetType, resultSetConcurrency, resultSetHoldability);
 }
	 
@Override
public PreparedStatement prepareStatement(final String sql, final int resultSetType, final int resultSetConcurrency, final int resultSetHoldability) throws SQLException {
    return new ShardingPreparedStatement(this, sql, resultSetType, resultSetConcurrency, resultSetHoldability);
}
</code></pre>
<p>同时，ShardingConnection 中包含了用于管理分布式事务的 ShardingTransactionManager。关于分布式事务的讨论不是今天的重点，我们后面会有专题来做详细展开。</p>
<p>但我们可以先看一下 commit 和 rollback 方法：</p>
<pre><code>@Override
public void commit() throws SQLException {
    if (TransactionType.LOCAL == transactionType) {
        super.commit();
    } else {
        shardingTransactionManager.commit();
    }
}

@Override
public void rollback() throws SQLException {
    if (TransactionType.LOCAL == transactionType) {
        super.rollback();
    } else {
        shardingTransactionManager.rollback();
    }
}
</code></pre>
<p>可以看到这两个方法的逻辑还是比较清晰的，即当事务类型为本地事务时直接调用 ShardingConnection 父类 AbstractConnectionAdapter 中的 commit 和 rollback 方法，这两个方法会调用真正的 connection 的相关方法。</p>
<p>以 commit 方法为例，我们可以看到 AbstractConnectionAdapter 中基于这一设计思想的实现过程：</p>
<pre><code>@Override
public void commit() throws SQLException {
    forceExecuteTemplate.execute(cachedConnections.values(), new ForceExecuteCallback&lt;Connection&gt;() {

        @Override
        public void execute(final Connection connection) throws SQLException {
            connection.commit();
        }
    });
}
</code></pre>
<h3>ShardingDataSource</h3>
<p>我们知道在 JDBC 规范中，可以通过 DataSource 获取 Connection 对象。ShardingSphere 完全兼容 JDBC 规范，所以 ShardingConnection 的创建过程应该也是在对应的 DataSource 中，这个 DataSource 就是<strong>ShardingDataSource</strong>。</p>
<p>ShardingDataSource 类比较简单，其构造函数如下所示：</p>
<pre><code>public ShardingDataSource(final Map&lt;String, DataSource&gt; dataSourceMap, final ShardingRule shardingRule, final Properties props) throws SQLException {
    super(dataSourceMap);
    checkDataSourceType(dataSourceMap);
    runtimeContext = new ShardingRuntimeContext(dataSourceMap, shardingRule, props, getDatabaseType());
}
</code></pre>
<p>可以看到，ShardingRuntimeContext 这个上下文对象是在 ShardingDataSource 的构造函数中被创建的，而创建 ShardingConnection 的过程也很直接：</p>
<pre><code>@Override
public final ShardingConnection getConnection() {
    return new ShardingConnection(getDataSourceMap(), runtimeContext, TransactionTypeHolder.get());
}
</code></pre>
<p>在 ShardingDataSource 的实现上，也同样采用的是装饰器模式，所以它的类层结构也与 ShardingConnection 的类似。在 ShardingDataSource 的父类 AbstractDataSourceAdapter 中，主要的工作是完成 DatabaseType 的创建，核心方法 createDatabaseType 如下所示：</p>
<pre><code>private DatabaseType createDatabaseType(final DataSource dataSource) throws SQLException {
    if (dataSource instanceof AbstractDataSourceAdapter) {
        return ((AbstractDataSourceAdapter) dataSource).databaseType;
    }
    try (Connection connection = dataSource.getConnection()) {
        return DatabaseTypes.getDatabaseTypeByURL(connection.getMetaData().getURL());
    }
}
</code></pre>
<p>可以看到这里使用到了 DatabaseTypes 类，该类负责 DatabaseType 实例的动态管理。而在 ShardingSphere 中，DatabaseType 接口代表数据库类型：</p>
<pre><code>public interface DatabaseType {
    //获取数据库名称
	String getName();
	//获取 JDBC URL 的前缀
	Collection&lt;String&gt; getJdbcUrlPrefixAlias();
	//获取数据源元数据
    DataSourceMetaData getDataSourceMetaData(String url, String username);
}
</code></pre>
<p>可以想象 ShardingSphere 中针对各种数据库提供了 DatabaseType 接口的实现类，其中以 MySQLDatabaseType 为例：</p>
<pre><code>public final class MySQLDatabaseType implements DatabaseType {

    @Override
    public String getName() {
        return &quot;MySQL&quot;;
    }

    @Override
    public Collection&lt;String&gt; getJdbcUrlPrefixAlias() {
        return Collections.singletonList(&quot;jdbc:mysqlx:&quot;);
    }

    @Override
    public MySQLDataSourceMetaData getDataSourceMetaData(final String url, final String username) {
        return new MySQLDataSourceMetaData(url);
    }
}
</code></pre>
<p>上述代码中的 MySQLDataSourceMetaData 实现了 DataSourceMetaData 接口，并提供如下所示的对输入 url 的解析过程：</p>
<pre><code>public MySQLDataSourceMetaData(final String url) {
    Matcher matcher = pattern.matcher(url);
    if (!matcher.find()) {
        throw new UnrecognizedDatabaseURLException(url, pattern.pattern());
    }
    hostName = matcher.group(4);
    port = Strings.isNullOrEmpty(matcher.group(5)) ? DEFAULT_PORT : Integer.valueOf(matcher.group(5));
    catalog = matcher.group(6);
    schema = null;
}
</code></pre>
<p>显然，DatabaseType 用于保存与特定数据库元数据相关的信息，ShardingSphere 还基于 SPI 机制实现对各种 DatabaseType 实例的动态管理。</p>
<p>最后，我们来到 ShardingDataSourceFactory 工厂类，该类负责 ShardingDataSource 的创建：</p>
<pre><code>public final class ShardingDataSourceFactory {

    public static DataSource createDataSource(
            final Map&lt;String, DataSource&gt; dataSourceMap, final ShardingRuleConfiguration shardingRuleConfig, final Properties props) throws SQLException {
        return new ShardingDataSource(dataSourceMap, new ShardingRule(shardingRuleConfig, dataSourceMap.keySet()), props);
    }
}
</code></pre>
<p>我们在这里创建了 ShardingDataSource，同时发现 ShardingRule 的创建过程实际上也是在这里，通过传入的 ShardingRuleConfiguration 来构建一个新的 ShardingRule 对象。</p>
<p>一旦创建了 DataSource，我们就可以使用与 JDBC 规范完全兼容的 API，通过该 DataSource 完成各种 SQL 的执行。我们可以回顾 ShardingDataSourceFactory 的使用过程来加深对他的理解：</p>
<pre><code>public DataSource dataSource() throws SQLException {
     //创建分片规则配置类
    ShardingRuleConfiguration shardingRuleConfig = new ShardingRuleConfiguration();

    //创建分表规则配置类
    TableRuleConfiguration tableRuleConfig = new TableRuleConfiguration(&quot;user&quot;, &quot;ds${0..1}.user${0..1}&quot;);

    //创建分布式主键生成配置类
    Properties properties = new Properties();
    result.setProperty(&quot;worker.id&quot;, &quot;33&quot;);
    KeyGeneratorConfiguration keyGeneratorConfig = new KeyGeneratorConfiguration(&quot;SNOWFLAKE&quot;, &quot;id&quot;, properties);
    result.setKeyGeneratorConfig(keyGeneratorConfig);
    shardingRuleConfig.getTableRuleConfigs().add(tableRuleConfig);

    //根据年龄分库，一共分为 2 个库
   shardingRuleConfig.setDefaultDatabaseShardingStrategyConfig(new InlineShardingStrategyConfiguration(&quot;sex&quot;, &quot;ds${sex % 2}&quot;));

    //根据用户 id 分表，一共分为 2 张表
    shardingRuleConfig.setDefaultTableShardingStrategyConfig(new StandardShardingStrategyConfiguration(&quot;id&quot;, &quot;user${id % 2}&quot;));

    //通过工厂类创建具体的 DataSource
    return ShardingDataSourceFactory.createDataSource(createDataSourceMap(), shardingRuleConfig, new Properties());
}
</code></pre>
<p>一旦获取了目标 DataSource 之后，我们就可以使用 JDBC 中的核心接口来执行传入的 SQL 语句：</p>
<pre><code>List&lt;User&gt; getUsers(final String sql) throws SQLException {
    List&lt;User&gt; result = new LinkedList&lt;&gt;();
    try (Connection connection = dataSource.getConnection();
         PreparedStatement preparedStatement = connection.prepareStatement(sql);
         ResultSet resultSet = preparedStatement.executeQuery()) {
        while (resultSet.next()) {
            User user= new User();
            //省略设置 User 对象的赋值语句
            result.add(user);
        }
    }
    return result;
}
</code></pre>
<p>ShardingSphere 通过在准备阶段获取的连接模式，在执行阶段生成<strong>内存归并结果集</strong>或<strong>流式归并结果集</strong>，并将其传递至<strong>结果归并引擎</strong>，以进行下一步工作。</p>
<h3>从源码解析到日常开发</h3>
<p>基于<strong>适配器模式</strong>完成对 JDBC 规范的重写，是我们学习 ShardingSphere 框架非常重要的一个切入点，同样也是我们将这种模式应用到日常开发工作中的一个切入点。</p>
<p>适配器模式是作为两个不兼容的接口之间的桥梁。在业务系统中，我们经常会碰到需要与外部系统进行对接和集成的场景，这个时候为了保证内部系统的功能演进，能够独立于外部系统进行发展，一般都需要采用适配器模式完成两者之间的隔离。</p>
<p>当我们设计这种系统时，可以参考 JDBC 规范中的接口定义方式，以及 ShardingSphere 中基于这种接口定义方式，而完成适配的具体做法。</p>
<h3>小结与预告</h3>
<p>这是 ShardingSphere 执行引擎的最后一个课时，我们围绕执行引擎的上层组件，给出了以“ Sharding”作为前缀的各种 JDBC 规范中的核心接口实现类。</p>
<p>其中 ShardingStatement 和 ShardingPreparedStatement 直接依赖于上一课时介绍的 StatementExecutor 和 PreparedStatementExecutor；而 ShardingConnection 和 ShardingDataSource 则为我们使用执行引擎提供了入口。</p>
<p>这里给你留一道思考题：ShardingSphere 中，AbstractShardingPreparedStatementAdapter 的类层结构为什么会比 AbstractStatementAdapter 复杂很多？欢迎你在留言区与大家讨论，我将逐一点评解答。</p>
<p>现在，我们已经通过执行引擎获取了来自不同数据源的结果数据，对于查询语句而言，我们通常都需要对这些结果数据进行归并才能返回给客户端。在接下来的内容中，就让我们来分析一下 ShardingSphere 的归并引擎。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="22&#32;&#32;执行引擎：如何把握&#32;ShardingSphere&#32;中的&#32;Executor&#32;执行模型？（上）.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="24&#32;&#32;归并引擎：如何理解数据归并的类型以及简单归并策略的实现过程？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434c908f4d70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
