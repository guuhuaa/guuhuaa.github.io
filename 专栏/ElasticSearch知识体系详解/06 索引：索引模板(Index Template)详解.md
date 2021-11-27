<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>06 索引：索引模板(Index Template)详解.md</title>
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

                    <a class="current-tab" href="06&#32;索引：索引模板(Index&#32;Template)详解.md">06 索引：索引模板(Index Template)详解.md</a>
                    

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

                    
                    <a href="19&#32;资料：Awesome&#32;Elasticsearch.md">19 资料：Awesome Elasticsearch.md</a>

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
                        <div><h1>06 索引：索引模板(Index Template)详解</h1>
<h2>索引模板</h2>
<blockquote>
<p>索引模板是一种告诉Elasticsearch在创建索引时如何配置索引的方法。</p>
</blockquote>
<ul>
<li><strong>使用方式</strong></li>
</ul>
<p>在创建索引之前可以先配置模板，这样在创建索引（手动创建索引或通过对文档建立索引）时，模板设置将用作创建索引的基础。</p>
<h3>模板类型</h3>
<p>模板有两种类型：<strong>索引模板</strong>和<strong>组件模板</strong>。</p>
<ol>
<li><strong>组件模板</strong>是可重用的构建块，用于配置映射，设置和别名；它们不会直接应用于一组索引。</li>
<li><strong>索引模板</strong>可以包含组件模板的集合，也可以直接指定设置，映射和别名。</li>
</ol>
<h3>索引模板中的优先级</h3>
<ol>
<li>可组合模板优先于旧模板。如果没有可组合模板匹配给定索引，则旧版模板可能仍匹配并被应用。</li>
<li>如果使用显式设置创建索引并且该索引也与索引模板匹配，则创建索引请求中的设置将优先于索引模板及其组件模板中指定的设置。</li>
<li>如果新数据流或索引与多个索引模板匹配，则使用优先级最高的索引模板。</li>
</ol>
<h3>内置索引模板</h3>
<p>Elasticsearch具有内置索引模板，每个索引模板的优先级为100，适用于以下索引模式：</p>
<ol>
<li><code>logs-*-*</code></li>
<li><code>metrics-*-*</code></li>
<li><code>synthetics-*-*</code></li>
</ol>
<p>所以在涉及内建索引模板时，要避免索引模式冲突。更多可以参考<a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/index-templates.html">这里</a></p>
<h3>案例</h3>
<ul>
<li>首先<strong>创建两个索引组件模板</strong>：</li>
</ul>
<pre><code class="language-bash">PUT _component_template/component_template1
{
  &quot;template&quot;: {
    &quot;mappings&quot;: {
      &quot;properties&quot;: {
        &quot;@timestamp&quot;: {
          &quot;type&quot;: &quot;date&quot;
        }
      }
    }
  }
}

PUT _component_template/runtime_component_template
{
  &quot;template&quot;: {
    &quot;mappings&quot;: {
      &quot;runtime&quot;: { 
        &quot;day_of_week&quot;: {
          &quot;type&quot;: &quot;keyword&quot;,
          &quot;script&quot;: {
            &quot;source&quot;: &quot;emit(doc['@timestamp'].value.dayOfWeekEnum.getDisplayName(TextStyle.FULL, Locale.ROOT))&quot;
          }
        }
      }
    }
  }
}
</code></pre>
<p>执行结果如下</p>
<p><img src="assets/es-index-template-1.png" alt="img" /></p>
<ul>
<li><strong>创建使用组件模板的索引模板</strong></li>
</ul>
<pre><code class="language-bash">PUT _index_template/template_1
{
  &quot;index_patterns&quot;: [&quot;bar*&quot;],
  &quot;template&quot;: {
    &quot;settings&quot;: {
      &quot;number_of_shards&quot;: 1
    },
    &quot;mappings&quot;: {
      &quot;_source&quot;: {
        &quot;enabled&quot;: true
      },
      &quot;properties&quot;: {
        &quot;host_name&quot;: {
          &quot;type&quot;: &quot;keyword&quot;
        },
        &quot;created_at&quot;: {
          &quot;type&quot;: &quot;date&quot;,
          &quot;format&quot;: &quot;EEE MMM dd HH:mm:ss Z yyyy&quot;
        }
      }
    },
    &quot;aliases&quot;: {
      &quot;mydata&quot;: { }
    }
  },
  &quot;priority&quot;: 500,
  &quot;composed_of&quot;: [&quot;component_template1&quot;, &quot;runtime_component_template&quot;], 
  &quot;version&quot;: 3,
  &quot;_meta&quot;: {
    &quot;description&quot;: &quot;my custom&quot;
  }
}
</code></pre>
<p>执行结果如下</p>
<p><img src="assets/es-index-template-2.png" alt="img" /></p>
<ul>
<li>创建一个匹配<code>bar*</code>的索引<code>bar-test</code></li>
</ul>
<pre><code class="language-bash">PUT /bar-test
</code></pre>
<p>然后获取mapping</p>
<pre><code class="language-bash">GET /bar-test/_mapping
</code></pre>
<p>执行结果如下</p>
<p><img src="assets/es-index-template-3.png" alt="img" /></p>
<h2>模拟多组件模板</h2>
<blockquote>
<p>由于模板不仅可以由多个组件模板组成，还可以由索引模板自身组成；那么最终的索引设置将是什么呢？ElasticSearch设计者考虑到这个，提供了API进行模拟组合后的模板的配置。</p>
</blockquote>
<h3>模拟某个索引结果</h3>
<p>比如上面的template_1, 我们不用创建bar*的索引(这里模拟bar-pdai-test)，也可以模拟计算出索引的配置：</p>
<pre><code class="language-bash">POST /_index_template/_simulate_index/bar-pdai-test
</code></pre>
<p>执行结果如下</p>
<p><img src="assets/es-index-template-4.png" alt="img" /></p>
<h3>模拟组件模板结果</h3>
<p>当然，由于template_1模板是由两个组件模板组合的，我们也可以模拟出template_1被组合后的索引配置：</p>
<pre><code class="language-bash">POST /_index_template/_simulate/template_1
</code></pre>
<p>执行结果如下：</p>
<pre><code class="language-json">{
  &quot;template&quot; : {
    &quot;settings&quot; : {
      &quot;index&quot; : {
        &quot;number_of_shards&quot; : &quot;1&quot;
      }
    },
    &quot;mappings&quot; : {
      &quot;runtime&quot; : {
        &quot;day_of_week&quot; : {
          &quot;type&quot; : &quot;keyword&quot;,
          &quot;script&quot; : {
            &quot;source&quot; : &quot;emit(doc['@timestamp'].value.dayOfWeekEnum.getDisplayName(TextStyle.FULL, Locale.ROOT))&quot;,
            &quot;lang&quot; : &quot;painless&quot;
          }
        }
      },
      &quot;properties&quot; : {
        &quot;@timestamp&quot; : {
          &quot;type&quot; : &quot;date&quot;
        },
        &quot;created_at&quot; : {
          &quot;type&quot; : &quot;date&quot;,
          &quot;format&quot; : &quot;EEE MMM dd HH:mm:ss Z yyyy&quot;
        },
        &quot;host_name&quot; : {
          &quot;type&quot; : &quot;keyword&quot;
        }
      }
    },
    &quot;aliases&quot; : {
      &quot;mydata&quot; : { }
    }
  },
  &quot;overlapping&quot; : [ ]
}
</code></pre>
<h3>模拟组件模板和自身模板结合后的结果</h3>
<ul>
<li>新建两个模板</li>
</ul>
<pre><code class="language-bash">PUT /_component_template/ct1
{
  &quot;template&quot;: {
    &quot;settings&quot;: {
      &quot;index.number_of_shards&quot;: 2
    }
  }
}

PUT /_component_template/ct2
{
  &quot;template&quot;: {
    &quot;settings&quot;: {
      &quot;index.number_of_replicas&quot;: 0
    },
    &quot;mappings&quot;: {
      &quot;properties&quot;: {
        &quot;@timestamp&quot;: {
          &quot;type&quot;: &quot;date&quot;
        }
      }
    }
  }
}
</code></pre>
<p>模拟在两个组件模板的基础上，添加自身模板的配置</p>
<pre><code class="language-bash">POST /_index_template/_simulate
{
  &quot;index_patterns&quot;: [&quot;my*&quot;],
  &quot;template&quot;: {
    &quot;settings&quot; : {
        &quot;index.number_of_shards&quot; : 3
    }
  },
  &quot;composed_of&quot;: [&quot;ct1&quot;, &quot;ct2&quot;]
}
</code></pre>
<p>执行的结果如下</p>
<pre><code class="language-json">{
  &quot;template&quot; : {
    &quot;settings&quot; : {
      &quot;index&quot; : {
        &quot;number_of_shards&quot; : &quot;3&quot;,
        &quot;number_of_replicas&quot; : &quot;0&quot;
      }
    },
    &quot;mappings&quot; : {
      &quot;properties&quot; : {
        &quot;@timestamp&quot; : {
          &quot;type&quot; : &quot;date&quot;
        }
      }
    },
    &quot;aliases&quot; : { }
  },
  &quot;overlapping&quot; : [ ]
}
</code></pre>
<p><img src="assets/es-index-template-5.png" alt="img" /></p>
<h2>参考文章</h2>
<p>https://www.elastic.co/guide/en/elasticsearch/reference/current/index-templates.html</p>
<p>https://www.elastic.co/guide/en/elasticsearch/reference/current/simulate-multi-component-templates.html</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="05&#32;索引：索引管理详解.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="07&#32;查询：DSL查询之复合查询详解.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b43401dbdc470ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
