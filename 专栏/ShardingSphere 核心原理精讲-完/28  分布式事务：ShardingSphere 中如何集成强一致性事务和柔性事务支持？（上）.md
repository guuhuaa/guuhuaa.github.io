<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>28  分布式事务：ShardingSphere 中如何集成强一致性事务和柔性事务支持？（上）.md</title>
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

                    <a class="current-tab" href="28&#32;&#32;分布式事务：ShardingSphere&#32;中如何集成强一致性事务和柔性事务支持？（上）.md">28  分布式事务：ShardingSphere 中如何集成强一致性事务和柔性事务支持？（上）.md</a>
                    

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
                        <div><h1>28  分布式事务：ShardingSphere 中如何集成强一致性事务和柔性事务支持？（上）</h1>
<p>今天我们将在上一课时的基础上，详细展开 ShardingSphere 中分布式事务的具体实现过程。首先，我们将介绍支持强一致性事务的 XAShardingTransactionManager。</p>
<h3>XAShardingTransactionManager</h3>
<p>让我们回到 ShardingSphere，来到 sharding-transaction-xa-core 工程的 XAShardingTransactionManager 类，该类是分布式事务的 XA 实现类。</p>
<p>我们先来看 XAShardingTransactionManager 类的定义和所包含的变量：</p>
<pre><code>public final class XAShardingTransactionManager implements ShardingTransactionManager {

    private final Map&lt;String, XATransactionDataSource&gt; cachedDataSources = new HashMap&lt;&gt;();

	private final XATransactionManager xaTransactionManager = XATransactionManagerLoader.getInstance().getTransactionManager();
	 
}
</code></pre>
<p>可以看到 XAShardingTransactionManager 实现了上一课时中介绍的 ShardingTransactionManager 接口，并保存着一组 XATransactionDataSource。同时，XATransactionManager 实例的加载仍然是采用了 JDK 中的 ServiceLoader 类，如下所示：</p>
<pre><code>private XATransactionManager load() {
        Iterator&lt;XATransactionManager&gt; xaTransactionManagers = ServiceLoader.load(XATransactionManager.class).iterator();
        if (!xaTransactionManagers.hasNext()) {
            return new AtomikosTransactionManager();
        }
        XATransactionManager result = xaTransactionManagers.next();
        if (xaTransactionManagers.hasNext()) {
            log.warn(&quot;There are more than one transaction mangers existing, chosen first one by default.&quot;);
        }
        return result;
}
</code></pre>
<p>XATransactionManager 就是对各种第三方 XA 事务管理器的一种抽象，通过上述代码，可以看到在找不到合适的 XATransactionManager 的情况下，系统默认会创建一个 AtomikosTransactionManager。而这个 XATransactionManager 的定义实际上是位于单独的一个代码工程中，即 sharding-transaction-xa-spi 工程，该接口定义如下所示：</p>
<pre><code>public interface XATransactionManager extends AutoCloseable {

    //初始化 XA 事务管理器
    void init();

    //注册事务恢复资源
    void registerRecoveryResource(String dataSourceName, XADataSource xaDataSource);

    //移除事务恢复资源
    void removeRecoveryResource(String dataSourceName, XADataSource xaDataSource);

    //嵌入一个 SingleXAResource 资源
    void enlistResource(SingleXAResource singleXAResource);

    //返回 TransactionManager
    TransactionManager getTransactionManager();
}
</code></pre>
<p>这些接口方法从命名上基本可以理解其含义，但详细的用法我们还是要结合具体的 XATransactionManager 实现类进行理解。这里我们还发现了一个 SingleXAResource，这个类同样位于 sharding-transaction-xa-spi 工程中，从名称上看，应该是对 JTA 中 XAResource 接口的一种实现，我们来看一下：</p>
<pre><code>public final class SingleXAResource implements XAResource {

    private final String resourceName;

    private final XAResource delegate;

    @Override
    public void start(final Xid xid, final int i) throws XAException {
        delegate.start(xid, i);
    } 
    @Override
    public void commit(final Xid xid, final boolean b) throws XAException {
        delegate.commit(xid, b);
    }

	@Override
    public void rollback(final Xid xid) throws XAException {
        delegate.rollback(xid);
    } 
    @Override
    public boolean isSameRM(final XAResource xaResource) {
        SingleXAResource singleXAResource = (SingleXAResource) xaResource;
        return resourceName.equals(singleXAResource.getResourceName());
	}
	…
}
</code></pre>
<p>可以看到 SingleXAResource 虽然实现了 JTA 的 XAResource 接口，但更像是一个代理类，具体的操作方法还是委托给了内部的 XAResource 进行实现。</p>
<p>接下来，我们将围绕 XA 分布式事务中的几个核心类展开讨论。</p>
<h4>1.XADataSource</h4>
<p>XADataSource 属于 JDBC 规范中的内容，我们在“03 | 规范兼容：JDBC 规范与 ShardingSphere 是什么关系？”中已经提到过这个接口，该接口的作用就是获取 XAConnection。</p>
<p>那么 XADataSource 是如何构建出来的呢？我们首先找到了一个 XADataSourceFactory 工厂类，显然该类负责生成具体的 XADataSource，如下所示的就是完成这一工作的 build 方法：</p>
<pre><code>public static XADataSource build(final DatabaseType databaseType, final DataSource dataSource) {
        XADataSourceDefinition xaDataSourceDefinition = XADataSourceDefinitionFactory.getXADataSourceDefinition(databaseType);
        XADataSource result = createXADataSource(xaDataSourceDefinition);
        Properties xaProperties = xaDataSourceDefinition.getXAProperties(SWAPPER.swap(dataSource));
        PropertyUtils.setProperties(result, xaProperties);
        return result;
}
</code></pre>
<p>这里首先用到了一个 XADataSourceDefinition 接口，从命名上看应该是关于 XADataSource 的一种定义，如下所示：</p>
<pre><code>public interface XADataSourceDefinition extends DatabaseTypeAwareSPI {

    //获取 XA 驱动类名
    Collection&lt;String&gt; getXADriverClassName();

    //获取 XA 属性
    Properties getXAProperties(DatabaseAccessConfiguration databaseAccessConfiguration);
}
</code></pre>
<p>可以看到这个接口继承了 DatabaseTypeAwareSPI，从命名上看这也是一个 SPI 接口，其定义如下所示：</p>
<pre><code>public interface DatabaseTypeAwareSPI { 
    //获取数据库类型
    String getDatabaseType();
}
</code></pre>
<p>在 ShardingSphere 中，继承 DatabaseTypeAwareSPI 接口的就只有 XADataSourceDefinition 接口，而后者存在一批实现类，整体的类层结构如下所示：</p>
<p><img src="assets/Ciqc1F9jCmiAI4cLAAE2ATnYWp4900.png" alt="Drawing 0.png" /></p>
<p>XADataSourceDefinition 的实现类</p>
<p>这里以 MySQLXADataSourceDefinition 为例展开讨论，该类分别实现了 DatabaseTypeAwareSPI 和 XADataSourceDefinition 这两个接口中所定义的三个方法：</p>
<pre><code>public final class MySQLXADataSourceDefinition implements XADataSourceDefinition {

    @Override
    public String getDatabaseType() {
        return &quot;MySQL&quot;;
    }

    @Override
    public Collection&lt;String&gt; getXADriverClassName() {
        return Arrays.asList(&quot;com.mysql.jdbc.jdbc2.optional.MysqlXADataSource&quot;, &quot;com.mysql.cj.jdbc.MysqlXADataSource&quot;);
    }

    @Override
    public Properties getXAProperties(final DatabaseAccessConfiguration databaseAccessConfiguration) {
        Properties result = new Properties();
        result.setProperty(&quot;user&quot;, databaseAccessConfiguration.getUsername());
        result.setProperty(&quot;password&quot;, Optional.fromNullable(databaseAccessConfiguration.getPassword()).or(&quot;&quot;));
        result.setProperty(&quot;URL&quot;, databaseAccessConfiguration.getUrl());
        … 
        return result;
    }
}
</code></pre>
<p>我们从这里得知，作为数据库供应商，MySQL 提供了两个 XADataSource 的驱动程序。而在 getXAProperties 中，我们发现 URL、Username 和 Password 等信息是通过 DatabaseAccessConfiguration 对象进行获取的，该对象在本文后面会介绍到。</p>
<p>另一方面，因为 DatabaseTypeAwareSPI 接口命名中带有 SPI，所以我们不难想象各种 XADataSourceDefinition 实际上也是基于 SPI 机制进行加载的，这在用于获取 XADataSourceDefinition 的工厂类 XADataSourceDefinitionFactory 中可以得到确认：</p>
<pre><code>public final class XADataSourceDefinitionFactory {

    private static final Map&lt;DatabaseType, XADataSourceDefinition&gt; XA_DATA_SOURCE_DEFINITIONS = new HashMap&lt;&gt;();

	static {
       //通过 ServiceLoader 加载 XADataSourceDefinition
        for (XADataSourceDefinition each : ServiceLoader.load(XADataSourceDefinition.class)) {
            XA_DATA_SOURCE_DEFINITIONS.put(DatabaseTypes.getActualDatabaseType(each.getDatabaseType()), each);
        }
    }

    public static XADataSourceDefinition getXADataSourceDefinition(final DatabaseType databaseType) {
        return XA_DATA_SOURCE_DEFINITIONS.get(databaseType);
    }
}
</code></pre>
<p>同样，在 sharding-transaction-xa-core 工程中，我们也发现了如下所示的 SPI 配置信息：</p>
<p><img src="assets/Ciqc1F9jCoWAOFRpAACUXKjEF6o633.png" alt="Drawing 1.png" /></p>
<p>sharding-transaction-xa-core 工程中的 SPI 配置</p>
<p>当根据数据库类型获取了对应的 XADataSourceDefinition 之后，我们就可以根据 XADriverClassName 来创建具体的 XADataSource：</p>
<pre><code>private static XADataSource loadXADataSource(final String xaDataSourceClassName) {
        Class xaDataSourceClass;
        try {
           //加载 XADataSource 实现类
            xaDataSourceClass = Thread.currentThread().getContextClassLoader().loadClass(xaDataSourceClassName);
        } catch (final ClassNotFoundException ignored) {
            try {
                xaDataSourceClass = Class.forName(xaDataSourceClassName);
            } catch (final ClassNotFoundException ex) {
                throw new ShardingException(&quot;Failed to load [%s]&quot;, xaDataSourceClassName);
            }
        }
        try {
            return (XADataSource) xaDataSourceClass.newInstance();
        } catch (final InstantiationException | IllegalAccessException ex) {
            throw new ShardingException(&quot;Failed to instance [%s]&quot;, xaDataSourceClassName);
        }
}
</code></pre>
<p>这里会先从当前线程的 ContextClassLoader 中加载目标驱动的实现类，如果加载不到，就直接通过反射进行创建，最后返回 XADataSource 的实例对象。</p>
<p>当获取了 XADataSource 的实例对象之后，我们需要设置它的属性，这部分工作是由 DataSourceSwapper 类来完成的。在这里，ShardingSphere 针对不同类型的数据库连接池工具还专门做了一层封装，提取了 DataSourcePropertyProvider 接口用于对 DataSource的URL 、Username 和 Password 等基础信息进行抽象。</p>
<p>DataSourcePropertyProvider 接口的定义如下所示：</p>
<pre><code>public interface DataSourcePropertyProvider {
    String getDataSourceClassName();
    String getURLPropertyName();
    String getUsernamePropertyName();
    String getPasswordPropertyName();
}
</code></pre>
<p>DataSourcePropertyProvider 的实现类有两个，一个是 DefaultDataSourcePropertyProvider，另一个是 HikariCPPropertyProvider。ShardingSphere 默认使用的是 HikariCPPropertyProvider，这点可以从如下所示的 SPI 配置文件中得到确认：</p>
<p><img src="assets/Ciqc1F9jCpSAGChUAAB8-cv8fCU688.png" alt="Drawing 2.png" /></p>
<p>DataSourcePropertyProvider 的 SPI 配置</p>
<p>HikariCPPropertyProvider 实现了 DataSourcePropertyProvider 接口，并包含了对这些基础信息的定义：</p>
<pre><code>public final class HikariCPPropertyProvider implements DataSourcePropertyProvider {

    @Override
    public String getDataSourceClassName() {
        return &quot;com.zaxxer.hikari.HikariDataSource&quot;;
    }

    @Override
    public String getURLPropertyName() {
        return &quot;jdbcUrl&quot;;
    }

    @Override
    public String getUsernamePropertyName() {
        return &quot;username&quot;;
    }

    @Override
    public String getPasswordPropertyName() {
        return &quot;password&quot;;
    }
}
</code></pre>
<p>然后在 DataSourceSwapper 的 swap 方法中，实际上就是通过反射来构建 findGetterMethod 工具方法，并以此获取 URL、Username 和 Password 等基础信息，并返回一个 DatabaseAccessConfiguration 对象供具体的 XADataSourceDefinition 进行使用。</p>
<p>swap 方法的实现如下所示：</p>
<pre><code>public DatabaseAccessConfiguration swap(final DataSource dataSource) {
        DataSourcePropertyProvider provider = DataSourcePropertyProviderLoader.getProvider(dataSource);
        try {
            String url = (String) findGetterMethod(dataSource, provider.getURLPropertyName()).invoke(dataSource);
            String username = (String) findGetterMethod(dataSource, provider.getUsernamePropertyName()).invoke(dataSource);
            String password = (String) findGetterMethod(dataSource, provider.getPasswordPropertyName()).invoke(dataSource);
            return new DatabaseAccessConfiguration(url, username, password);
        } catch (final ReflectiveOperationException ex) {
            throw new ShardingException(&quot;Cannot swap data source type: `%s`, please provide an implementation from SPI `%s`&quot;, 
                    dataSource.getClass().getName(), DataSourcePropertyProvider.class.getName());
        }
}
</code></pre>
<p>至此，我们对 XADataSource 的构建过程描述完毕。这个过程不算复杂，但涉及的类比较多，值得我们以 XADataSourceFactory 为中心画一张类图作为总结：</p>
<p><img src="assets/Ciqc1F9jCqGAYmlZAACYlVXsQ44048.png" alt="image.png" /></p>
<h4>2.XAConnection</h4>
<p>讲完 XADataSource，我们接着来讲 XAConnection，XAConnection 同样是 JDBC 规范中的接口。</p>
<p>负责创建 XAConnection 的工厂类 XAConnectionFactory 如下所示：</p>
<pre><code>public final class XAConnectionFactory { 
    //基于普通 Connection 创建 XAConnection 
    public static XAConnection createXAConnection(final DatabaseType databaseType, final XADataSource xaDataSource, final Connection connection) {
        switch (databaseType.getName()) {
            case &quot;MySQL&quot;:
                return new MySQLXAConnectionWrapper().wrap(xaDataSource, connection);
            case &quot;MariaDB&quot;:
                return new MariaDBXAConnectionWrapper().wrap(xaDataSource, connection);
            case &quot;PostgreSQL&quot;:
                return new PostgreSQLXAConnectionWrapper().wrap(xaDataSource, connection);
            case &quot;H2&quot;:
                return new H2XAConnectionWrapper().wrap(xaDataSource, connection);
            default:
                throw new UnsupportedOperationException(String.format(&quot;Cannot support database type: `%s`&quot;, databaseType));
        }
    }
}
</code></pre>
<p>可以看到，相较 XADataSource，创建 XAConnection 的过程就显得直接明了。这里通过一个 switch 语句根据数据库类型分别构建了对应的 ConnectionWrapper，然后再调用 wrap 方法返回 XAConnection。</p>
<p>我们还是以 MySQLXAConnectionWrapper 为例来分析具体的实现过程。</p>
<p>MySQLXAConnectionWrapper 实现了 XAConnectionWrapper 接口，所以我们先来看 XAConnectionWrapper 接口的定义：</p>
<pre><code>public interface XAConnectionWrapper { 
    //基于 XADataSource 把 Connection 包装成 XAConnection
    XAConnection wrap(XADataSource xaDataSource, Connection connection);
}
</code></pre>
<p>XAConnectionWrapper 接口只有一个方法，即根据传入的 XADataSource 和一个普通 Connection 对象创建出一个新的 XAConnection 对象。XAConnectionWrapper 接口的类层结构如下所示：</p>
<p><img src="assets/Ciqc1F9jCrCAXTkWAAD4zJLBg8I622.png" alt="Drawing 4.png" /></p>
<p>XAConnectionWrapper 接口的实现类</p>
<p>MySQLXAConnectionWrapper 中的 warp 方法如下所示：</p>
<pre><code>@Override
public XAConnection wrap(final XADataSource xaDataSource, final Connection connection) {
        //获取真实 Connection 对象
        Connection physicalConnection = unwrapPhysicalConnection(xaDataSource.getClass().getName(), connection);
        Method method = xaDataSource.getClass().getDeclaredMethod(&quot;wrapConnection&quot;, Connection.class);
        method.setAccessible(true);
       //通过反射包装 Connection 对象
        return (XAConnection) method.invoke(xaDataSource, physicalConnection);
}
</code></pre>
<p>上述方法的流程为先通过 unwrapPhysicalConnection 将传入的 Connection 转变为一个真实的连接对象，然后再基于 XADataSource 的 wrapConnection 方法通过反射对这个物理连接进行包装，从而形成一个 XAConnection 对象。</p>
<p>对于 Mysql 而言，我们在前面的内容中已经知道它有两种 XADataSource 驱动类。而在 MySQLXAConnectionWrapper 我们同样找到了如下所示的这两种驱动类的类名定义：</p>
<pre><code>private static final String MYSQL_XA_DATASOURCE_5 = &quot;com.mysql.jdbc.jdbc2.optional.MysqlXADataSource&quot;;

private static final String MYSQL_XA_DATASOURCE_8 = &quot;com.mysql.cj.jdbc.MysqlXADataSource&quot;;
</code></pre>
<p>显然，根据数据库版本的不同，这两个驱动类的行为也有所不同。因此，unwrapPhysicalConnection 的处理过程如下所示：</p>
<pre><code>private Connection unwrapPhysicalConnection(final String xaDataSourceClassName, final Connection connection) {
        switch (xaDataSourceClassName) {
            case MYSQL_XA_DATASOURCE_5:
                return (Connection) connection.unwrap(Class.forName(&quot;com.mysql.jdbc.Connection&quot;));
            case MYSQL_XA_DATASOURCE_8:
                return (Connection) connection.unwrap(Class.forName(&quot;com.mysql.cj.jdbc.JdbcConnection&quot;));
            default:
                throw new UnsupportedOperationException(String.format(&quot;Cannot support xa datasource: `%s`&quot;, xaDataSourceClassName));
        }
}
</code></pre>
<p>作为对比，我们再来看 PostgreSQLXAConnectionWrapper，它的 wrap 方法则比较简单，如下所示。显然，这部分内容的理解需要对不同的数据库驱动有一定的了解。</p>
<pre><code>public XAConnection wrap(final XADataSource xaDataSource, final Connection connection) {
        BaseConnection physicalConnection = (BaseConnection) connection.unwrap(Class.forName(&quot;org.postgresql.core.BaseConnection&quot;));
        return new PGXAConnection(physicalConnection);
}
</code></pre>
<h4>3.XATransactionDataSource</h4>
<p>介绍完了 XADataSource 和 XAConnection 的创建过程之后，让我们回到 XAShardingTransactionManager，我们发现这里用到的 DataSource 并不是 JDBC 中原生的 XADataSource，而是一种 XATransactionDataSource。</p>
<p>我们来到这个 XATransactionDataSource 类，该类的变量和构造函数如下所示：</p>
<pre><code>private final DatabaseType databaseType;
private final String resourceName;
private final DataSource dataSource;
private XADataSource xaDataSource;
private XATransactionManager xaTransactionManager; 
	 
public XATransactionDataSource(final DatabaseType databaseType, final String resourceName, final DataSource dataSource, final XATransactionManager xaTransactionManager) {
        this.databaseType = databaseType;
        this.resourceName = resourceName;
        this.dataSource = dataSource;
        if (!CONTAINER_DATASOURCE_NAMES.contains(dataSource.getClass().getSimpleName())) {
            this.xaDataSource = XADataSourceFactory.build(databaseType, dataSource);
            this.xaTransactionManager = xaTransactionManager;
            xaTransactionManager.registerRecoveryResource(resourceName, xaDataSource);
        }
}
</code></pre>
<p>上述变量我们都认识，而在构造函数中，调用了 XATransactionManager 类中的 registerRecoveryResource 方法将构建的 XADataSource 作为一种资源进行注册。</p>
<p>然后，我们来看 XATransactionDataSource 中的核心方法 getConnection，如下所示：</p>
<pre><code>public Connection getConnection() throws SQLException, SystemException, RollbackException {
        if (CONTAINER_DATASOURCE_NAMES.contains(dataSource.getClass().getSimpleName())) {
            return dataSource.getConnection();
        }
        //从DataSource中 构建一个 Connection
        Connection result = dataSource.getConnection();
        //通过 XAConnectionFactory 创建一个 XAConnection
        XAConnection xaConnection = XAConnectionFactory.createXAConnection(databaseType, xaDataSource, result);
        //从 XATransactionManager 中获取 Transaction 对象
        final Transaction transaction = xaTransactionManager.getTransactionManager().getTransaction();
        //判当前线程中是否存在这个 Transaction
        if (!enlistedTransactions.get().contains(transaction)) {
         //将 XAConnection 中的 XAResource 与目标 Transaction 对象关联起来
            transaction.enlistResource(new SingleXAResource(resourceName, xaConnection.getXAResource()));
            //Transaction 中注册一个 Synchronization 接口
            transaction.registerSynchronization(new Synchronization() {
                @Override
                public void beforeCompletion() {
                    enlistedTransactions.get().remove(transaction);
                }

                @Override
                public void afterCompletion(final int status) {
                    enlistedTransactions.get().clear();
                }
            });
            //将该 Transaction 对象放入到当前线程中
            enlistedTransactions.get().add(transaction);
        }
        return result;
}
</code></pre>
<p>这里先从 DataSource 中构建一个 Connection，然后传入到 XAConnectionFactory 中创建一个 XAConnection，接着从 XATransactionManager 中获取 Transaction 对象。请注意在 XATransactionDataSource 中存在一个 ThreadLocal 变量 enlistedTransactions，用于保存当前线程所涉及的 Transaction 对象列表：</p>
<pre><code>private final ThreadLocal&lt;Set&lt;Transaction&gt;&gt; enlistedTransactions = new ThreadLocal&lt;Set&lt;Transaction&gt;&gt;() {
        @Override
        public Set&lt;Transaction&gt; initialValue() {
            return new HashSet&lt;&gt;();
        }
};
</code></pre>
<p>在上述方法中，当从 XATransactionManager 中获取 Transaction 对象之后，会先判断 enlistedTransactions中 是否存在该 Transaction 对象，如果没有，则将 XAConnection 中的 XAResource 与目标 Transaction 对象关联起来。</p>
<p>然后我们再来看 Transaction 对象的 registerSynchronization 方法的使用方法，该方法注册了一个 Synchronization 接口，该接口包含了 beforeCompletion 和 afterCompletion 这两个方法。</p>
<p>在二阶段提交之前，TransctionManager 会调用 Synchronization 接口的 beforeCompletion 方法；而当事务结束时，TransctionManager 会调用 Synchronization 接口的 afterCompletion方法。我们在 getConnection 方法中看到这两个方法的应用。最终，我们把该 Transaction 对象放入到线程安全的 enlistedTransactions 中。</p>
<p>最后，我们来看一下 XATransactionDataSource 的 close 方法，如下所示：</p>
<pre><code>@Override
public void close() {
        if (!CONTAINER_DATASOURCE_NAMES.contains(dataSource.getClass().getSimpleName())) {
            xaTransactionManager.removeRecoveryResource(resourceName, xaDataSource);
        } else {
            close(dataSource);
        }
}
</code></pre>
<p>可以看到，这里调用了 XATransactionManager 的 removeRecoveryResource 方法将资源进行移出。</p>
<p>至此，基于 XATransactionDataSource 获取 Connection 的过程也介绍完毕。关于 XATransactionManager的 具体内容我们放在下一课时中继续进行探讨。</p>
<h3>从源码解析到日常开发</h3>
<p>ShardingSphere 作为一款完全兼容 JDBC 规范的分布式数据库中间件，同样完成了针对分布式事务中的相关对象的兼容。今天的课程中，进一步强化了我们对 JDBC 规范的理解和如何扩展JDBC 规范中核心接口的方法。同时，在 MySQLXAConnectionWrapper 这个 Wrapper 类中，我们也再次看到使用反射技术创建 XAConnection 对象的实现方法。这些开发技巧都值得我们进行学习和应用。</p>
<h3>小结与预告</h3>
<p>分布式事务是一个相对复杂的概念，ShardingSphere 中提供了强一致性和最终一致性两种实现方案。今天的内容我们围绕基于 XA 协议的分片事务管理器 XAShardingTransactionManager 展开了讨论，在理解 XAShardingTransactionManager 中 XADataSource、XAConnection 等核心对象时，重点还是需要站在 JDBC 规范的基础上，掌握与分布式事务集成和兼容的整个过程，本课时对这一过程进行了详细的介绍。</p>
<p>这里给你留一道思考题：ShardingSphere 中对分布式环境下的强一致性事务做了哪些维度的抽象？欢迎你在留言区与大家讨论，我将逐一点评解答。</p>
<p>XAShardingTransactionManager 的内容很多，下一课时，我们将在今天课时的基础上，继续探讨 XAShardingTransactionManager 的剩余部分内容，以及 ShardingSphere 中另一个分片事务管理器 SeataATShardingTransactionManager。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="27&#32;&#32;分布式事务：如何理解&#32;ShardingSphere&#32;中对分布式事务的抽象过程？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="29&#32;&#32;分布式事务：ShardingSphere&#32;中如何集成强一致性事务和柔性事务支持？（下）.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434caa0e8870ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
