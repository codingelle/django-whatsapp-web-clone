pipeline {
  agent { label "sweetheart" }
  environment {
    MYHOME = "$HOME/Documents/django-whatsapp-web-clone"
  }
  stages {
    stage("Build") {
      steps {
        sh "git clone https://github.com/codingelle/django-whatsapp-web-clone.git"  
        dir("django-whatsapp-web-clone"){
            sh "podman build -t django-app ."
        }
        sh """
            podman pod create -n ci-pod -p 8081:80 -p 8082:8082 -p 6379:6379 -p 5432:5432
            podman run --pod=ci-pod -d --name redis-svc registry.redhat.io/rhel8/redis-5:1-160.1647451816
            podman run --pod=ci-pod -d --name postgres-svc --env-file=$MYHOME/.env registry.redhat.io/rhel8/postgresql-12:1-99.1647451835
            podman run --pod=ci-pod -d --name app-svc --env-file=$MYHOME/.env localhost/django-app:latest
        """
      }
    }

    stage("Test") {
      steps {
        sh 'podman exec -ti app-svc bash -c "python manage.py test"'
      }
    }

    stage("Deploy") {
      steps {
        echo "Deploy here"
      }
    }
  }
  post {
    // Clean after build
    always {
        cleanWs()
        sh "podman pod rm ci-pod -f"
    }
    success {
        echo "Build success"
    }
    failure {
        echo "Build failed"
    }
  }
}
