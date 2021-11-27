<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>19 资料：Awesome Elasticsearch.md</title>
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

                    
                    <a href="01&#32;认知：ElasticSearch基础概念.md">01 认知：ElasticSearch基础概念.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;认知：Elastic&#32;Stack生态和场景方案.md">02 认知：Elastic Stack生态和场景方案.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;安装：ElasticSearch和Kibana安装.md">03 安装：ElasticSearch和Kibana安装.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;入门：查询和聚合的基础使用.md">04 入门：查询和聚合的基础使用.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;索引：索引管理详解.md">05 索引：索引管理详解.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;索引：索引模板(Index&#32;Template)详解.md">06 索引：索引模板(Index Template)详解.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;查询：DSL查询之复合查询详解.md">07 查询：DSL查询之复合查询详解.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;查询：DSL查询之全文搜索详解.md">08 查询：DSL查询之全文搜索详解.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;查询：DSL查询之Term详解.md">09 查询：DSL查询之Term详解.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;聚合：聚合查询之Bucket聚合详解.md">10 聚合：聚合查询之Bucket聚合详解.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;聚合：聚合查询之Metric聚合详解.md">11 聚合：聚合查询之Metric聚合详解.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;聚合：聚合查询之Pipline聚合详解.md">12 聚合：聚合查询之Pipline聚合详解.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;原理：从图解构筑对ES原理的初步认知.md">13 原理：从图解构筑对ES原理的初步认知.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;原理：ES原理知识点补充和整体结构.md">14 原理：ES原理知识点补充和整体结构.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;原理：ES原理之索引文档流程详解.md">15 原理：ES原理之索引文档流程详解.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;原理：ES原理之读取文档流程详解.md">16 原理：ES原理之读取文档流程详解.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;优化：ElasticSearch性能优化详解.md">17 优化：ElasticSearch性能优化详解.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;大厂实践：腾讯万亿级&#32;Elasticsearch&#32;技术实践.md">18 大厂实践：腾讯万亿级 Elasticsearch 技术实践.md</a>

                </li>
                <li>

                    <a class="current-tab" href="19&#32;资料：Awesome&#32;Elasticsearch.md">19 资料：Awesome Elasticsearch.md</a>
                    

                </li>
                <li>

                    
                    <a href="20&#32;WrapperQuery.md">20 WrapperQuery.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;备份和迁移.md">21 备份和迁移.md</a>

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
                        <div><h1>19 资料：Awesome Elasticsearch</h1>
<h1>General</h1>
<h2>Elastic Stack</h2>
<ul>
<li><a href="https://www.elastic.co/">Elasticsearch </a>official website</li>
<li><a href="https://www.elastic.co/products/logstash">Logstash </a>is a data pipeline that helps you process logs and other event data from a variety of systems</li>
<li><a href="https://www.elastic.co/products/kibana">Kibana </a>is a data analysis tool that helps to visualize your data; <a href="https://www.elastic.co/guide/en/kibana/current/discover.html">Kibana Manual docs</a></li>
<li><a href="https://www.elastic.co/products/beats">beats </a>is the platform for building lightweight, open source data shippers for many types of data you want to enrich with Logstash, search and analyze in Elasticsearch, and visualize in Kibana.</li>
</ul>
<h2>Books</h2>
<ul>
<li><a href="https://www.manning.com/books/deep-learning-for-search">Deep Learning for Search </a>- teaches you how to leverage neural networks, NLP, and deep learning techniques to improve search performance. (2019)</li>
<li><a href="https://www.manning.com/books/relevant-search">Relevant Search: with applications for Solr and Elasticsearch </a>- demystifies relevance work. Using Elasticsearch, it teaches you how to return engaging search results to your users, helping you understand and leverage the internals of Lucene-based search engines. (2016)</li>
<li><a href="https://www.manning.com/books/elasticsearch-in-action">Elasticsearch in Action </a>- teaches you how to build scalable search applications using Elasticsearch (2015)</li>
</ul>
<h2>Related (awesome) lists</h2>
<ul>
<li><a href="https://github.com/frutik/awesome-search">frutik/awesome-search </a>I am building e-commerce search now. Below are listed some of my build blocks</li>
</ul>
<h2>Open-source and free products, based on Elasticsearch</h2>
<ul>
<li><a href="https://fess.codelibs.org/index.html">Fess </a>is an open source full featured Enterprise Search, with a web-crawler</li>
<li><a href="https://github.com/yelp/elastalert">Yelp/elastalert </a>is a modular flexible rules based alerting system written in Python</li>
<li><a href="https://github.com/etsy/411">etsy/411 </a>- an Alert Management Web Application https://demo.fouroneone.io (credentials: user/user)</li>
<li><a href="https://github.com/appbaseio/mirage">appbaseio/mirage </a>is a 🔎 GUI for composing Elasticsearch queries</li>
<li><a href="https://github.com/exceptionless/Exceptionless">exceptionless/Exceptionless </a>is an error (exceptions) collecting and reporting server with client bindings for a various programming languages</li>
<li><a href="https://github.com/searchkit/searchkit">searchkit/searchkit </a>is a UI framework based on React to build awesome search experiences with Elasticsearch</li>
<li><a href="https://opensource.appbase.io/reactivemaps">appbaseio/reactivemaps </a>is a React based UI components library for building Airbnb / Foursquare like Maps</li>
<li><a href="https://opensource.appbase.io/reactivesearch">appbaseio/reactivesearch </a>is a library of beautiful React UI components for Elasticsearch</li>
<li><a href="https://github.com/appbaseio/dejavu/">appbaseio/dejavu </a>The missing UI for Elasticsearch; <a href="https://opensource.appbase.io/dejavu/">landing page</a></li>
<li><a href="https://github.com/pitchpoint-solutions/sfs">Simple File Server </a>is an Openstack Swift compatible distributed object store that can serve and securely store billions of large and small files using minimal resources.</li>
<li><a href="https://www.npmjs.com/package/@sematext/logagent">logagent </a>a log shipper to parse and ship logs to Elasticsearch including bulk indexing, disk buffers and log format detection.</li>
<li><a href="https://github.com/itemsapi/itemsapi">ItemsAPI </a>simplified search API for web and mobile (based on Elasticsearch and Express.js)</li>
<li><a href="https://github.com/kuzzleio/kuzzle">Kuzzle </a>- An open-source backend with advanced real-time features for Web, Mobile and IoT that uses ElasticSearch as a database. (<a href="https://kuzzle.io/">Website </a>)</li>
<li><a href="https://github.com/citybasebrooks/SIAC">SIAC </a>- SIAC is an enterprise SIEM built on the ELK stack and other open-source components.</li>
<li><a href="https://github.com/sirensolutions/sentinl">Sentinl </a>- Sentinl is a Kibana alerting and reporting app.</li>
<li><a href="https://github.com/ServerCentral/praeco/">Praeco </a>- Elasticsearch alerting made simple</li>
</ul>
<h2>Elasticsearch developer tools and utilities</h2>
<h3>Development and debugging</h3>
<ul>
<li><a href="https://github.com/elastic/sense/#sense">Sense (from Elastic) </a>A JSON aware developer console to Elasticsearch; official and very powerful</li>
<li><a href="https://github.com/dakrone/es-mode">ES-mode </a>An Emacs major mode for interacting with Elasticsearch (similar to Sense)</li>
<li><a href="http://elasticsearch-cheatsheet.jolicode.com/">Elasticsearch Cheatsheet </a>Examples for the most used queries, API and settings for all major version of Elasticsearch</li>
<li><a href="https://github.com/objectrocket/elasticstat">Elasticstat </a>CLI tool displaying monitoring informations like htop</li>
<li><a href="https://github.com/hsen-dev/vscode-elastic">Elastic for Visual Studio Code </a>An extension for developing Elasticsearch queries like Kibana and Sense extention in Visual Studio Code</li>
<li><a href="https://github.com/sudo-suhas/elastic-builder">Elastic Builder </a>A Node.js implementation of the Elasticsearch DSL</li>
<li><a href="https://github.com/danpaz/bodybuilder">Bodybuilder </a>A Node.js elasticsearch query body builder</li>
<li><a href="https://github.com/kelp404/enju">enju </a>A Node.js elasticsearch ORM</li>
<li><a href="https://github.com/ywangd/peek">Peek </a>An interactive CLI in Python that works like Kibana Console with additional features</li>
</ul>
<h3>Import and Export</h3>
<ul>
<li><a href="https://github.com/jprante/elasticsearch-knapsack">Knapsack plugin </a>is an &quot;swiss knife&quot; export/import plugin for Elasticsearch</li>
<li><a href="https://github.com/mallocator/Elasticsearch-Exporter">Elasticsearch-Exporter </a>is a command line script to import/export data from Elasticsearch to various other storage systems</li>
<li><a href="https://github.com/miku/esbulk">esbulk </a>Parallel elasticsearch bulk indexing utility for the command line.</li>
<li><a href="https://github.com/taskrabbit/elasticsearch-dump">elasticdump </a>- tools for moving and saving indices</li>
<li><a href="https://github.com/moshe/elasticsearch_loader">elasticsearch-loader </a>- Tool for loading common file types to elasticsearch including csv, json, and parquet</li>
</ul>
<h3>Management</h3>
<ul>
<li><a href="https://github.com/jeromepin/esctl">Esctl </a>- High-level command line interface to manage Elasticsearch clusters.</li>
<li><a href="https://github.com/github/vulcanizer">Vulcanizer </a>- Github's open sourced cluster management library based on Elasticsearch's REST API. Comes with a high level CLI tool</li>
</ul>
<h2>Elasticsearch plugins</h2>
<h3>Cluster</h3>
<ul>
<li><a href="https://github.com/sscarduzio/elasticsearch-readonlyrest-plugin">sscarduzio/elasticsearch-readonlyrest-plugin </a>Safely expose Elasticsearch REST API directly to the public</li>
<li><a href="https://github.com/mobz/elasticsearch-head">mobz/elasticsearch-head </a>is a powerful and essential plugin for managing your cluster, indices and mapping</li>
<li><a href="http://bigdesk.org/">Bigdesk </a>- Live charts and statistics for elasticsearch cluster</li>
<li><a href="http://www.elastichq.org/">Elastic HQ </a>- Elasticsearch cluster management console with live monitoring and beautiful UI</li>
<li><a href="https://github.com/lmenezes/cerebro">Cerebro </a>is an open source(MIT License) elasticsearch web admin tool. Supports ES 5.x</li>
<li><a href="https://github.com/lmenezes/elasticsearch-kopf">Kopf </a>- Another management plugin that have REST console and <em>manual</em> shard allocation</li>
<li><a href="https://github.com/floragunncom/search-guard">Search Guard </a>- Elasticsearch and elastic stack security and alerting for free</li>
<li><a href="https://github.com/NVISO-BE/ee-outliers">ee-outliers </a>- ee-outliers is a framework to detect outliers in events stored in an Elasticsearch cluster.</li>
<li><a href="https://github.com/moshe/elasticsearch-comrade">Elasticsearch Comrade </a>- Elasticsearch admin panel built for ops and monitoring</li>
<li><a href="https://github.com/stephanediondev/elasticsearch-admin">elasticsearch-admin </a>- Web administration for Elasticsearch</li>
</ul>
<h3>Other</h3>
<ul>
<li><a href="https://github.com/sirensolutions/siren-join">SIREn Join Plugin for Elasticsearch </a>This plugin extends Elasticsearch with new search actions and a filter query parser that enables to perform a &quot;Filter Join&quot; between two set of documents (in the same index or in different indexes).</li>
</ul>
<h3>Integrations and SQL support</h3>
<ul>
<li><a href="https://github.com/NLPchina/elasticsearch-sql/">NLPchina/elasticsearch-sql </a>- Query elasticsearch using familiar SQL syntax. You can also use ES functions in SQL.</li>
<li><a href="https://github.com/elastic/elasticsearch-hadoop">elastic/elasticsearch-hadoop </a>- Elasticsearch real-time search and analytics natively integrated with Hadoop (and Hive)</li>
<li><a href="https://github.com/jprante/elasticsearch-jdbc">jprante/elasticsearch-jdbc </a>- JDBC importer for Elasticsearch</li>
<li><a href="https://github.com/onesuper/pandasticsearch">pandasticsearch </a>- An Elasticsearch client exposing DataFrame API</li>
<li><a href="https://github.com/rwynn/monstache">monstache </a>- Go daemon that syncs MongoDB to Elasticsearch in near realtime</li>
</ul>
<h3>You know, for search</h3>
<ul>
<li><a href="https://github.com/jprante/elasticsearch-plugin-bundle">jprante/elasticsearch-plugin-bundle </a>A plugin that consists of a compilation of useful Elasticsearch plugins related to indexing and searching documents</li>
</ul>
<h2>Kibana plugins and applications</h2>
<ul>
<li><a href="https://github.com/elastic/timelion">elastic/timelion </a>time-series analyses application. Overview and installation guide: Timelion: <a href="https://www.elastic.co/blog/timelion-timeline">The time series composer for Kibana</a></li>
<li><a href="https://github.com/elasticfence/kaae">Kibana Alert App for Elasticsearch </a>- Kibana plugin with monitoring, alerting and reporting capabilities</li>
<li><a href="https://github.com/austin-taylor/VulnWhisperer">VulnWhisperer </a>- VulnWhisperer is a vulnerability data and report aggregator.</li>
<li><a href="https://github.com/wazuh/wazuh-kibana-app">Wazuh Kibana App </a>- A Kibana app for working with data generated by <a href="https://wazuh.com/">Wazuh </a>.</li>
<li><a href="https://github.com/datasweet-fr/kibana-datasweet-formula">Datasweet Formula </a>- A real time calculated metric plugin <a href="http://www.datasweet.fr/datasweet-formula/">Datasweet Formula </a>.</li>
</ul>
<h3>Kibana Visualization plugins</h3>
<ul>
<li><a href="https://github.com/nbs-system/mapster">nbs-system/mapster </a>- a visualization which allows to create live event 3d maps in Kibana</li>
<li><a href="https://github.com/stormpython/tagcloud">Kibana Tag Cloud Plugin </a>- tag cloud visualization plugin based on d3-cloud plugin</li>
<li><a href="https://github.com/sivasamyk/logtrail">LogTrail </a>- a plugin for Kibana to view, analyze, search and tail log events from multiple hosts in realtime with devops friendly interface inspired by Papertrail</li>
<li><a href="https://github.com/johtani/analyze-api-ui-plugin">Analyze API </a>- Kibana 6 application to manipulate the <code>_analyze</code> API graphically</li>
<li><a href="https://github.com/dlumbrer/kbn_network">kbn_network </a>- This is a plugin developed for Kibana that displays a network node that link two fields that have been previously selected.</li>
</ul>
<h2>Discussions and social media</h2>
<ul>
<li><a href="https://www.reddit.com/r/elasticsearch">/r/elasticsearch</a></li>
<li><a href="https://discuss.elastic.co/">Elasticsearch forum</a></li>
<li><a href="https://stackoverflow.com/tags/elasticsearch/hot">Stackoverflow</a></li>
<li><a href="https://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Daps&amp;field-keywords=elasticsearch">Books on Amazon </a>does not fit well into this category, but worth checking out!</li>
<li>TODO: Put some good twitter accounts</li>
</ul>
<h2>Tutorials</h2>
<ul>
<li><a href="https://www.digitalocean.com/community/tutorial_series/centralized-logging-with-logstash-and-kibana-on-ubuntu-14-04">Centralized Logging with Logstash and Kibana On Ubuntu 14.04 </a>everything you need to now when you are creating your first Elasticsearch+Logstash+Kibana instance</li>
<li><a href="https://github.com/dwyl/learn-elasticsearch">dwyl/learn-elasticsearch </a>a getting started tutorial with a pack of valuable references</li>
<li><a href="https://www.youtube.com/watch?v=8vgTBIoF8zs">Make Sense of your Logs: From Zero to Hero in less than an Hour! by Britta Weber </a>demonstrates how you can build Elasticsearch + Logstash + Kibana stack to collect and discover your data</li>
<li><a href="https://www.manning.com/livevideo/elasticsearch-7-and-elastic-stack">$$ Elasticsearch 7 and Elastic Stack </a>- liveVideo course that teaches you to search, analyze, and visualize big data on a cluster with Elasticsearch, Logstash, Beats, Kibana, and more.</li>
</ul>
<h2>Articles</h2>
<h2>System configuration</h2>
<ul>
<li><a href="http://logz.io/blog/elasticsearch-cheat-sheet/">A Useful Elasticsearch Cheat Sheet in Times of Trouble</a></li>
<li><a href="http://code972.com/blog/2014/07/74-the-definitive-guide-for-elasticsearch-on-windows-azure">The definitive guide for Elasticsearch on Windows Azure</a></li>
<li><a href="https://asquera.de/blog/2012-11-25/elasticsearch-pre-flight-checklist/">Elasticsearch pre-flight checklist</a></li>
<li><a href="https://www.loggly.com/blog/nine-tips-configuring-elasticsearch-for-high-performance/">9 Tips on Elasticsearch Configuration for High Performance</a></li>
<li><a href="https://www.elastic.co/guide/en/elasticsearch/plugins/master/cloud-aws-best-practices.html">Best Practices in AWS</a></li>
<li><a href="https://www.mapr.com/blog/how-secure-elasticsearch-and-kibana">How to Secure Elasticsearch and Kibana </a>with NGINX, LDAP and SSL 🔒</li>
<li><a href="http://joanswork.com/webfaction-elasticsearch-server-tutorial/">Elasticsearch server on Webfaction using NGINX with basic authorization and HTTPS protocol</a></li>
<li><a href="https://opster.com/elasticsearch-guides/">Elasticsearch Guides </a>Useful Elasticsearch guides with best practices, troubleshooting instructions for errors, tips, examples of code snippets and more.</li>
</ul>
<h3>Docker and Elasticsearch</h3>
<ul>
<li><a href="https://stefanprodan.com/2016/elasticsearch-cluster-with-docker/">Running an Elasticsearch cluster with Docker</a></li>
</ul>
<h2>Java tuning</h2>
<ul>
<li><a href="https://jprante.github.io/2012/11/28/Elasticsearch-Java-Virtual-Machine-settings-explained.html">Elasticsearch Java Virtual Machine settings explained</a></li>
<li><a href="https://live.mgm-tp.com/en/tuning-garbage-collection-for-mission-critical-java-applications-tuning-guidelines-for-java-garbage-collection-part-1/">Tuning Garbage Collection for Mission-Critical Java Applications</a></li>
<li><a href="http://www.infoq.com/articles/G1-One-Garbage-Collector-To-Rule-Them-All">G1: One Garbage Collector To Rule Them All</a></li>
<li><a href="http://blog.thetaphi.de/">Use Lucene’s MMapDirectory on 64bit platforms, please!</a></li>
<li><a href="https://product.hubspot.com/blog/g1gc-tuning-your-hbase-cluster">Black Magic cookbook</a></li>
<li><a href="https://product.hubspot.com/blog/g1gc-fundamentals-lessons-from-taming-garbage-collection">G1GC Fundamentals: Lessons from Taming Garbage Collection</a></li>
<li><a href="https://tigase.tech/attachments/download/4808/GC-result.pdf">JVM Garbage Collector settings investigation </a>PDF Comparison of JVM GC</li>
<li><a href="https://dzone.com/articles/garbage-collection-settings-for-elasticsearch-mast">Garbage Collection Settings for Elasticsearch Master Nodes </a>Fine tunine your garbage collector</li>
<li><a href="https://dzone.com/articles/understanding-g1-gc-log-format">Understanding G1 GC Log Format </a>To tune and troubleshoot G1 GC enabled JVMs, one must have a proper understanding of G1 GC log format. This article walks through key things that one should know about the G1 GC log format.</li>
</ul>
<p>How to start using G1</p>
<pre><code class="language-text">#ES_JAVA_OPTS=&quot;&quot;
ES_JAVA_OPTS=&quot;-XX:-UseParNewGC -XX:-UseConcMarkSweepGC -XX:+UseG1GC&quot;
</code></pre>
<h2>Scalable Infrastructure and performance</h2>
<ul>
<li><a href="https://qbox.io/blog/authoritative-guide-elasticsearch-performance-tuning-part-1">The Authoritative Guide to Elasticsearch Performance Tuning (Part 1) </a><a href="https://qbox.io/blog/elasticsearch-performance-tuning-part-2-zen">Part 2 </a><a href="https://qbox.io/index.php?p=blog/authoritative-guide-elasticsearch-performance-tuning-part-3">Part 3</a></li>
<li><a href="https://azure.microsoft.com/en-us/documentation/articles/guidance-elasticsearch-tuning-data-ingestion-performance/">Tuning data ingestion performance for Elasticsearch on Azure </a>- and not only for Azure. That's a great article about Elasticsearch Performance testing by example</li>
<li><a href="https://blog.codecentric.de/en/2014/05/elasticsearch-indexing-performance-cheatsheet/">Elasticsearch Indexing Performance Cheatsheet </a>- when you plan to index large amounts of data in Elasticsearch (by Patrick Peschlow)</li>
<li><a href="http://edgeofsanity.net/article/2012/12/26/elasticsearch-for-logging.html">Elasticsearch for Logging </a>Elasticsearch configuration tips and tricks from Sanity</li>
<li><a href="https://engineeringblog.yelp.com/2014/11/scaling-elasticsearch-to-hundreds-of-developers.html">Scaling Elasticsearch to Hundreds of Developers </a>by Joseph Lynch @yelp</li>
<li><a href="http://radar.oreilly.com/2015/04/10-elasticsearch-metrics-to-watch.html">10 Elasticsearch metrics to watch</a></li>
<li><a href="https://joshrendek.com/2015/11/understanding-elasticsearch-performance/">Understanding Elasticsearch Performance</a></li>
<li><a href="http://www.cubrid.org/blog/dev-platform/our-experience-creating-large-scale-log-search-system-using-elasticsearch/">Our Experience of Creating Large Scale Log Search System Using Elasticsearch </a>- topology, separate master, data and search balancers nodes</li>
<li>📂 <a href="https://github.com/Azure/azure-content/blob/master/articles/guidance/guidance-elasticsearch.md">Elasticsearch on Azure Guidance </a>it is 10% on Azure and 90% of a very valuable general information, tips and tricks about Elasticsearch</li>
<li><a href="http://blog.trifork.com/2013/10/24/how-to-avoid-the-split-brain-problem-in-elasticsearch/">How to avoid the split-brain problem in Elasticsearch</a></li>
<li>Datadog's series about monitoring Elasticsearch performance:
<ul>
<li><a href="https://www.datadoghq.com/blog/monitor-elasticsearch-performance-metrics/">How to monitor Elasticsearch performance</a></li>
<li><a href="https://www.datadoghq.com/blog/collect-elasticsearch-metrics/">How to collect Elasticsearch metrics</a></li>
<li><a href="https://www.datadoghq.com/blog/monitor-elasticsearch-datadog/">How to monitor Elasticsearch with Datadog</a></li>
<li><a href="https://www.datadoghq.com/blog/elasticsearch-performance-scaling-problems/">How to solve 5 Elasticsearch performance and scaling problems</a></li>
</ul>
</li>
<li><a href="https://sematext.com/publications/performance-monitoring-essentials-elasticsearch-edition.pdf">Performance Monitoring Essentials - Elasticsearch Edition</a></li>
<li><a href="https://github.com/zalando-incubator/es-operator">Operator for running Elasticsearch in Kubernetes</a></li>
</ul>
<h3>Integrations</h3>
<ul>
<li><a href="https://www.elastic.co/guide/en/elasticsearch/hadoop/current/hive.html">Apache Hive integration</a></li>
<li><a href="http://ryrobes.com/systems/connecting-tableau-to-elasticsearch-read-how-to-query-elasticsearch-with-hive-sql-and-hadoop/">Connecting Tableau to Elasticsearch (READ: How to query Elasticsearch with Hive SQL and Hadoop)</a></li>
<li><a href="https://github.com/mradamlacey/elasticsearch-tableau-connector">mradamlacey/elasticsearch-tableau-connector</a></li>
</ul>
<h3>Logging</h3>
<ul>
<li><a href="https://sematext.com/blog/2016/09/13/logstash-alternatives/">5 Logstash Alternatives </a>and typical use cases</li>
</ul>
<h3>Alerts</h3>
<ul>
<li><a href="https://engineeringblog.yelp.com/2015/10/elastalert-alerting-at-scale-with-elasticsearch.html">ElastAlert: Alerting At Scale With Elasticsearch, Part 1 </a>by engineeringblog.yelp.com</li>
<li><a href="https://engineeringblog.yelp.com/2016/03/elastalert-part-two.html">ElastAlert: Alerting At Scale With Elasticsearch, Part 2 </a>by engineeringblog.yelp.com</li>
<li><a href="https://alexandreesl.com/2016/04/15/elastalert-implementing-rich-monitoring-with-elasticsearch/">Elastalert: implementing rich monitoring with Elasticsearch</a></li>
</ul>
<h3>Time series</h3>
<ul>
<li><a href="https://www.elastic.co/blog/elasticsearch-as-a-time-series-data-store">Elasticsearch as a Time Series Data Store </a>by Felix Barnsteiner</li>
<li><a href="https://www.elastic.co/blog/out-of-this-world-aggregations">Running derivatives on Voyager velocity data </a>By Colin Goodheart-Smithe</li>
<li>Shewhart Control Charts via Moving Averages: <a href="https://www.elastic.co/blog/staying-in-control-with-moving-averages-part-1">Part 1 </a>- <a href="https://www.elastic.co/blog/staying-in-control-with-moving-averages-part-2">Part 2 </a>by Zachary Tong</li>
<li>Implementing a Statistical Anomaly Detector: <a href="https://www.elastic.co/blog/implementing-a-statistical-anomaly-detector-part-1">Part 1 </a>- <a href="https://www.elastic.co/blog/implementing-a-statistical-anomaly-detector-part-2">Part 2 </a>- <a href="https://www.elastic.co/blog/implementing-a-statistical-anomaly-detector-part-3">Part 3 </a>by Zachary Tong</li>
</ul>
<h3>Machine Learning</h3>
<ul>
<li><a href="http://www.deepdetect.com/tutorials/es-image-classifier/">Classifying images into Elasticsearch with DeepDetect </a>(<a href="https://discuss.elastic.co/t/categorizing-images-with-deep-learning-into-elasticsearch/33217">forum thread with discussion </a>) by Emmanuel Benazera</li>
<li><a href="https://medium.com/hello-elasticsearch/elasticsearch-amazon-machine-learning-7d7b979c328d#.s50a6d5mn">Elasticsearch with Machine Learning </a>(<a href="https://translate.googleusercontent.com/translate_c?depth=1&amp;hl=en&amp;prev=search&amp;rurl=translate.google.com&amp;sl=ja&amp;u=https://medium.com/hello-elasticsearch/elasticsearch-amazon-machine-learning-7d7b979c328d&amp;usg=ALkJrhioEPGsVRglGPFTa6w2ZfM-ydSoeg">English translation </a>) by Kunihiko Kido</li>
<li><a href="https://www.mapr.com/products/mapr-sandbox-hadoop/tutorials/recommender-tutorial">Recommender System with Mahout and Elasticsearch</a></li>
</ul>
<h3>Use cases for Elasticsearch</h3>
<ul>
<li><a href="http://engineering.ifttt.com/data/2015/10/14/data-infrastructure/">Data Infrastructure at IFTTT </a>Elasticsearch, Kafka, Apache Spark, Redhsift, other AWS services</li>
<li><a href="https://israelwebdev.wordpress.com/2015/01/19/ofac-compliance-with-elasticsearch/">OFAC compliance with Elasticsearch </a>using AWS</li>
<li><a href="https://blog.insightdatascience.com/building-a-streaming-search-platform-61a0d5a323a8#.f4b0rvae5">Building a Streaming Search Platform </a>- Streaming Search on Tweets: Storm, Elasticsearch, and Redis</li>
</ul>
<h2>Other</h2>
<ul>
<li><a href="https://packetzoom.com/blog/logzoom-a-fast-and-lightweight-substitute-for-logstash.html">LogZoom, a fast and lightweight substitute for Logstash</a></li>
<li><a href="https://github.com/Graylog2/graylog2-server">Graylog2/graylog2-server </a>- Free and open source log management (based on ES)</li>
<li><a href="http://www.slideshare.net/td-nttcom/fluentd-vs-logstash-for-openstack-log-management">Fluentd vs. Logstash for OpenStack Log Management</a></li>
<li><a href="http://david.pilato.fr/blog/2015/12/10/building-a-directory-map-with-elk/">Building a Directory Map With ELK</a></li>
<li><a href="http://engineering.laterooms.com/structured-logging-with-elk-part-1/">Structured logging with ELK - part 1</a></li>
<li><a href="http://jolicode.com/blog/search-for-emoji-with-elasticsearch">Search for 😋 Emoji with Elasticsearch 🔎</a></li>
<li><a href="http://logz.io/learn/complete-guide-elk-stack/">Complete Guide to the ELK Stack</a></li>
<li><a href="https://github.com/sloniki/logiq">logiq </a>- Simple WebUI Monitoring Tool for Logstash ver. 5.0 and up</li>
<li><a href="https://malike.github.io/elasticsearch-report-engine/">ElasticSearch Report Engine </a>- An ElasticSearch plugin to return query results as either PDF,HTML or CSV.</li>
<li><a href="https://opster.com/elasticsearch-glossary/">Elasticsearch Glossary </a>- explanations of Elasticsearch terminology, including examples, common best practices and troubleshooting guides for various issues.</li>
</ul>
<h2>Videos</h2>
<h3>Overviews</h3>
<ul>
<li><a href="https://www.youtube.com/watch?v=44QQEI9CJQQ">Elasticsearch for logs and metrics: A deep dive – Velocity 2016 </a>by Sematext Developers</li>
<li><a href="https://www.youtube.com/watch?v=oPObRc8tHgQ">Elasticsearch in action Thijs Feryn </a>a beginner overview</li>
<li><a href="https://www.youtube.com/watch?v=7FLXjgB0PQI">Getting Down and Dirty with ElasticSearch by Clinton Gormley </a></li>
<li><a href="https://raygun.io/blog/2014/05/talk-how-we-scaled-raygun-using-technologies-like-elastic-search-featuring-iron-man/">How we scaled Raygun</a></li>
<li><a href="https://www.youtube.com/watch?v=60UsHHsKyN4&amp;list=PLw5h0DiJ-9PDStvJYc1LOZiEm1ehlEKLP">Getting started with Elasticsearch</a></li>
<li><a href="https://www.youtube.com/watch?v=vruklYSW4jg">Speed is a Key: Elasticsearch under the Hood </a>introduction + basic performance optimization</li>
<li><a href="https://www.pluralsight.com/courses/elasticsearch-for-dotnet-developers">$$ Pluralsight: Getting Started With Elasticsearch for .NET Developers </a>this course will introduce users to Elasticsearch, how it works, and how to use it with .NET projects.</li>
<li><a href="https://www.udemy.com/elasticsearch-complete-guide/">$$ Complete Guide to Elasticsearch </a>Comprehensive guide to Elasticsearch, the popular search engine built on Apache Lucene</li>
<li><a href="http://www.infoq.com/presentations/elasticsearch-guardian">How Elasticsearch powers the Guardian's newsroom</a></li>
<li><a href="https://www.youtube.com/watch?v=hEztaMtobXw">Elasticsearch Query Editor in Grafana</a></li>
<li><a href="https://www.youtube.com/watch?v=pZJLlOCuPpg">Scale Your Metrics with Elasticsearch </a>2019 by Philipp Krenn (Elastic) optimization tips and tricks</li>
</ul>
<h3>Advanced</h3>
<ul>
<li><a href="https://www.youtube.com/watch?v=eQ-rXP-D80U">#bbuzz 2015: Adrien Grand – Algorithms and data-structures that power Lucene and Elasticsearch</a></li>
<li><a href="https://www.youtube.com/watch?list=PLq-odUc2x7i_-qsarQo7MNsrYz3rlXGMu&amp;v=D2zR-6Tke8o">Rafał Kuć - Running High Performance Fault-tolerant Elasticsearch Clusters on Docker </a>and <a href="https://sematext.com/blog/2016/06/08/elasticsearch-in-docker/">slides</a></li>
<li><a href="http://shop.oreilly.com/product/0636920043898.do">Working with Elasticsearch - Search, Aggregate, Analyze, and Scale Large Volume Datastores </a>- O'Reilly Media</li>
<li><a href="https://www.youtube.com/watch?v=sa_Y488vj0M">End-to-end Recommender System with Spark and Elasticsearch </a>by Nick Pentreath &amp; Jean-François Puget. <a href="http://www.slideshare.net/sparktc/spark-ml-meedup-pentreath-puget">Slide deck</a></li>
</ul>
<h3>Code, configuration file samples and other gists</h3>
<ul>
<li><a href="https://gist.github.com/reyjrar/4364063">Elasticsearch config for a write-heavy cluster </a>- reyjrar/elasticsearch.yml</li>
<li><a href="https://github.com/chenryn/ESPL">chenryn/ESPL - Elastic Search Processing Language </a>PEG parser sample for SPL to Elasticsearch DSL</li>
<li><a href="https://github.com/thomaspatzke/EQUEL">thomaspatzke/EQUEL </a>an Elasticsearch QUEry Language, based on G4 grammar parser</li>
</ul>
<h2>Who is using elasticsearch?</h2>
<p><a href="https://engineeringblog.yelp.com/2015/10/how-we-use-deep-learning-to-classify-business-photos-at-yelp.html">Yelp </a>, <a href="http://engineering.ifttt.com/data/2015/10/14/data-infrastructure/">IFTTT </a>, <a href="https://stackexchange.com/performance">StackExchange </a>, <a href="https://raygun.io/blog/2014/02/search-improvements-at-raygun/">Raygun </a>, <a href="https://www.youtube.com/watch?v=lWKEphKIG8U">Mozilla </a>, <a href="https://labs.spotify.com/2015/11/17/monitoring-at-spotify-introducing-heroic/">Spotify </a>, <a href="https://medium.com/@ghoranyi/needle-in-a-haystack-873c97a99983">CERN </a>, <a href="https://www.elastic.co/elasticon/2015/sf/unlocking-interplanetary-datasets-with-real-time-search">NASA </a><a href="https://www.elastic.co/fr/videos/creating-the-fashion-experience-of-the-future-with-elasticsearch-at-zalando">Zalando</a></p>
<h2>I want more! (Elasticsearch related resources)</h2>
<ul>
<li><a href="https://alexandreesl.com/">Technology Explained Blog</a></li>
<li><a href="http://blog.eagerelk.com/">EagerElk</a></li>
<li><a href="https://www.timroes.de/">Tim Roes Blog</a></li>
</ul>
<h1>Contributing</h1>
<ul>
<li>Make sure you are about to post a valuable resource that belongs to this list</li>
<li>Do NOT group ++Add and --Remove changes in same PR. Make them separate pull requests</li>
<li>Use spellchecker</li>
<li>All spelling and grammar corrections are welcome (except for the rule above)</li>
<li>Fork this repo, do your edits, send the pull request</li>
<li>Feel free to create any new sections</li>
<li>Do not even try to add this repo to any awesome-awesome-* lists</li>
</ul>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="18&#32;大厂实践：腾讯万亿级&#32;Elasticsearch&#32;技术实践.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="20&#32;WrapperQuery.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b43406d9b5970ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/ElasticSearch%E7%9F%A5%E8%AF%86%E4%BD%93%E7%B3%BB%E8%AF%A6%E8%A7%A3/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
