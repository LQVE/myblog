KindEditor.ready(function(K) {
                K.create('#textarea[name=content]',{
                    width:'700px',
                    height:'320px',
                    uploadJson:'/admin/upload/kindeditor',
                });
        });