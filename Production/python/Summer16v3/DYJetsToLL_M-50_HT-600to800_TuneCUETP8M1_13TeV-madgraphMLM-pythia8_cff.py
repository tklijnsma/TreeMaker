import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/00B225C5-64EB-E811-AEDB-0025905A60B0.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/06174A66-39EB-E811-A8A3-0025905A6076.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/0C770727-46EB-E811-8E14-0CC47A7C345C.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/0E33D4A6-3BEB-E811-9388-0CC47A78A3F4.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/0ED6C900-3AEB-E811-BA4D-0CC47A4C8F26.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/1084249F-4FEB-E811-A69A-0025905B8606.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/180D3F6D-58EB-E811-8528-0CC47A78A3F8.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/1C36700E-C7EB-E811-9A94-001E67A3FD26.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/1C3B0880-54EB-E811-A12B-0CC47A4D7692.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/2012A775-49EB-E811-A9EC-0CC47A4D7646.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/228AEADE-99EC-E811-9FE1-0CC47A7C3434.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/26E11638-51EB-E811-A2DA-0CC47A4D76D6.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/2A7C2E03-48EB-E811-9EE7-0CC47A7C34B0.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/3CAFA4E8-38EB-E811-B2D4-0CC47A4C8E98.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/44A0B76A-3CEB-E811-BD04-0CC47A4D7646.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/46A8241E-3AEB-E811-8BCC-0CC47A4C8F10.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/48D81F9F-4FEB-E811-90FE-0025905B8606.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/5241BB45-3BEB-E811-8544-0CC47A7C357A.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/5E9DBE6C-3AEB-E811-9A76-0CC47A7C357E.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/64764B92-3FEB-E811-A0C5-0CC47A74524E.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/760972D6-24EC-E811-B31B-0CC47A4C8EE8.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/78081F7C-3BEB-E811-B44F-0CC47A7C345E.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/78B6B47C-51EB-E811-B3E2-0CC47A7C34D0.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/82C7CC88-3AEB-E811-942B-0CC47A78A446.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/8663D6DB-38EB-E811-8311-0CC47A7C35C8.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/88692BF0-3AEB-E811-8C7F-0CC47A4D76D0.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/96F0B673-41EB-E811-B598-0CC47A745284.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/9CF6597F-54EB-E811-9DA6-0CC47A4D7636.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/A245159F-9BEC-E811-A54D-0025905A48C0.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/B65EC011-BAEC-E811-98BE-0CC47A4D76B2.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/B8F945EF-3DEB-E811-8521-0025905A6134.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/BAA3BDD8-3AEB-E811-B9E1-0025905A6082.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/BAAFCE53-4DEB-E811-81AC-0CC47A7C354A.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/C2971C52-4DEB-E811-99C3-0CC47A4C8E28.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/CC37CBFA-37EB-E811-A32C-0CC47A7C3412.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/CEE8E769-3AEB-E811-BC0E-0CC47A7C357A.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/D03E6986-3AEB-E811-9804-0CC47A4C8E8A.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/D87B3DBE-39EB-E811-8CE5-0CC47A78A3D8.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/DE55B0D1-9AEC-E811-B1C5-0025905A60E4.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/E080F98F-10ED-E811-8A76-003048FFD722.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/E461B543-6DEB-E811-BFAA-0CC47A4D7650.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/E4FD6C51-39EB-E811-AE87-0025905A6066.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/E650D56E-ADEC-E811-846E-0CC47A4D7670.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/EA05AD10-C6EC-E811-94D7-0025905A6134.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/F63FF7F3-3AEB-E811-9B6C-0CC47A4C8E98.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/0E4DB0AA-5FEB-E811-8637-0CC47A7C3434.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/12EAF1EE-42EB-E811-9993-EC0D9A0B3370.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/1AA86629-3CEB-E811-8772-0CC47A78A4A0.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/1C0B1BEB-51EB-E811-A261-A4BF01025C02.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/1ED2B849-41EB-E811-A8A7-0025905A608C.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/1EE20B59-3DEB-E811-959D-0CC47A4C8F10.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/20976E35-42EB-E811-A923-002590593920.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/289BF551-42EB-E811-A9FE-0CC47A4C8F2C.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/2AE59F23-43EB-E811-815F-90B11C070100.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/30C24533-41EB-E811-893E-A4BF01027688.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/3C59ADD7-41EB-E811-A430-001E67A3F70E.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/3C84BC94-45EB-E811-B700-0025905A60EE.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/3E6D2E99-43EB-E811-B1BD-0CC47A78A3EC.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/445D8030-41EB-E811-93E4-0CC47A4D76C0.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/44CE8821-59EB-E811-8B4C-0CC47A7C345E.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/505DFF7C-3CEB-E811-80BA-EC0D9A0B3330.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/52AE03FE-4AEB-E811-B44E-001E67DDC88A.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/54BE431A-41EB-E811-A5E0-0CC47A4D7636.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/5C0E68A4-44EB-E811-A098-0025905A60A0.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/5EEC4608-AEEB-E811-A5A2-0CC47A4D7654.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/66E3708B-43EB-E811-963E-0025905A6076.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/6A87F714-45EB-E811-B69B-0025905AA9CC.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/6ADEC2AF-5FEB-E811-8328-0CC47A4C8F06.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/6E048269-49EB-E811-B617-0CC47A7C356A.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/7A407DAE-43EB-E811-BB58-0025905A48C0.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/7CE2222C-63EB-E811-A537-001E67DDC6C8.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/7E88B167-4BEB-E811-B507-0025905B8560.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/827D0BDE-40EB-E811-B029-EC0D9A0B30D0.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/82C27D73-3FEB-E811-A4D2-0CC47A4C8E26.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/8E6DCE28-3CEB-E811-9D7F-0CC47A7C3638.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/8E85F69D-40EB-E811-8223-001E67A3FE66.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/9052449A-40EB-E811-83E5-0025905A60A6.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/90563221-59EB-E811-9A86-0CC47A4C8E1E.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/92B85A9B-43EB-E811-8C59-001E67DFF519.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/98286657-42EB-E811-A45B-90B11C06CD59.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/9E769861-43EB-E811-B338-001E67DDD0AA.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/9EE5D493-3DEB-E811-8595-0CC47A4C8E28.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/A483FD1B-3EEB-E811-B208-0CC47A4C8E8A.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/A492473F-3FEB-E811-A776-0025905B85D8.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/A6C1590F-40EB-E811-8F5C-0CC47A78A3EC.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/A89D9614-43EB-E811-88FE-0CC47A4D762E.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/AAEFCB41-41EB-E811-B846-001E67DDC6C8.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/AC289CE0-41EB-E811-A4DB-EC0D9A0B32F0.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/AE693986-3EEB-E811-A36F-0CC47A78A436.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/B0C1178A-43EB-E811-B5FF-0025905A610A.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/B27BD66A-42EB-E811-839E-0CC47A4C8E34.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/B6615439-1FEC-E811-A706-0CC47A4C8E1C.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/C403DA9F-3DEB-E811-B4AC-0CC47A7C354C.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/CA1C3D6D-43EB-E811-9379-0025905B8592.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/D4B98B9A-43EB-E811-875E-0CC47A745250.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/D69F9097-4FEB-E811-81EE-001E67DFF5D7.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/DA806CAF-44EB-E811-8A45-0025905A6064.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/DC38E30C-6BEB-E811-B696-0CC47A4D76C0.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/DCC6DEC9-51EB-E811-A2CB-0CC47A7C347E.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/E0027ADC-40EB-E811-BD06-0CC47A7C3638.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/E8A246AD-5FEB-E811-84D8-0CC47A4D76C0.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/F870F613-43EB-E811-8CD6-0CC47A4C8E34.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/FE82E30E-43EB-E811-AE9D-EC0D9A0B3340.root',
] )
